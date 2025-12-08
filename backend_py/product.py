from flask import Blueprint, request, jsonify
from config import get_connection
import os
import traceback
from werkzeug.utils import secure_filename
import time
import uuid

product_bp = Blueprint("products_admin", __name__)

# Thư mục lưu ảnh (tương đối so với file này)
# Kết quả: backend_py/image/products/<file>
BASE_DIR = os.path.dirname(__file__)
UPLOAD_ROOT = os.path.join(BASE_DIR, "image", "products")
os.makedirs(UPLOAD_ROOT, exist_ok=True)

# Các định dạng cho phép
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@product_bp.get("/admin/products")
def admin_get_products():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM sanphams")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@product_bp.post("/admin/products")
def admin_add_product():
    d = request.json
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO sanphams (tenSanPham, gia, moTa, anh, soLuong, trangThai)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (
        d.get("tenSanPham"), d.get("gia"), d.get("moTa"), d.get("anh"),
        d.get("soLuong"), d.get("trangThai")
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Tạo sản phẩm thành công"})

# DELETE product - xóa file ảnh nếu có
@product_bp.delete("/admin/products/<int:id>")
def delete_product(id):
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        # Lấy thông tin ảnh hiện tại để xóa file trên disk nếu có
        cur.execute("SELECT anh FROM sanphams WHERE id=%s", (id,))
        row = cur.fetchone()

        # Xóa file trên disk nếu tồn tại
        if row and row.get("anh"):
            img_path = row["anh"]  # ví dụ '/images/products/xxx.jpg' hoặc 'products/xxx.jpg' hoặc chỉ filename
            # chuẩn hoá thành đường dẫn trong folder image
            # nếu img_path bắt đầu bằng '/images/', bỏ tiền tố
            rel = img_path
            if rel.startswith("/images/"):
                rel = rel[len("/images/"):]  # 'products/xxx.jpg'
            # đảm bảo không có ../
            rel = rel.replace("/", os.sep)
            file_on_disk = os.path.join(BASE_DIR, "image", rel)
            try:
                if os.path.exists(file_on_disk):
                    os.remove(file_on_disk)
                    print("Deleted image file:", file_on_disk)
            except Exception as exf:
                print("Could not delete image file:", exf)

        # Xóa record DB
        cur.execute("DELETE FROM sanphams WHERE id=%s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"msg": "Xóa sản phẩm thành công"})
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"msg": "Lỗi khi xóa product", "error": str(ex)}), 500


@product_bp.put("/admin/products/<int:id>")
def update_product(id):
    try:
        d = request.json or {}
        if not d:
            return jsonify({"msg": "Không có dữ liệu cập nhật"}), 400

        # Nếu có cập nhật ảnh -> lấy ảnh cũ để xóa sau khi update thành công
        old_img = None
        if "anh" in d:
            conn_tmp = get_connection()
            cur_tmp = conn_tmp.cursor(dictionary=True)
            cur_tmp.execute("SELECT anh FROM sanphams WHERE id=%s", (id,))
            r = cur_tmp.fetchone()
            if r:
                old_img = r.get("anh")
            cur_tmp.close()
            conn_tmp.close()

        # build câu lệnh động
        fields = []
        vals = []
        mapping = {
            "tenSanPham": "tenSanPham",
            "gia": "gia",
            "moTa": "moTa",
            "anh": "anh",
            "soLuong": "soLuong",
            "trangThai": "trangThai"
        }
        for key, col in mapping.items():
            if key in d:
                fields.append(f"{col}=%s")
                vals.append(d[key])

        if not fields:
            return jsonify({"msg":"Không có trường hợp hợp lệ để cập nhật"}), 400

        vals.append(id)
        sql = "UPDATE sanphams SET " + ", ".join(fields) + " WHERE id=%s"

        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql, tuple(vals))
        conn.commit()
        cur.close()
        conn.close()

        # nếu có ảnh cũ và khác ảnh mới -> xóa file cũ
        if old_img and "anh" in d:
            new_img = d.get("anh") or ""
            if old_img != new_img:
                rel = old_img
                if rel.startswith("/images/"):
                    rel = rel[len("/images/"):]
                rel = rel.replace("/", os.sep)
                file_on_disk = os.path.join(BASE_DIR, "image", rel)
                try:
                    if os.path.exists(file_on_disk):
                        os.remove(file_on_disk)
                        print("Deleted old image file after update:", file_on_disk)
                except Exception as exf:
                    print("Could not delete old image file:", exf)

        return jsonify({"msg":"Cập nhật sản phẩm thành công"})
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"msg":"Lỗi khi cập nhật product", "error": str(ex)}), 500


@product_bp.post("/admin/upload-image")
def admin_upload_image():
    """
    Nhận file từ client (field name 'image'), lưu vào folder image/products,
    trả về JSON { ok: True, url: "/images/products/xxx.jpg" }
    """
    try:
        if 'image' not in request.files:
            return jsonify({"ok": False, "msg": "Không tìm thấy file"}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({"ok": False, "msg": "Tên file rỗng"}), 400

        if not allowed_file(file.filename):
            return jsonify({"ok": False, "msg": "Không hỗ trợ định dạng file"}), 400

        # chuẩn hóa filename
        filename = secure_filename(file.filename)
        name_part, ext = os.path.splitext(filename)
        filename = f"{name_part}_{int(time.time())}_{uuid.uuid4().hex[:6]}{ext}"

        save_path = os.path.join(UPLOAD_ROOT, filename)
        file.save(save_path)

        # trả về đường dẫn client có thể truy cập (matching route /images/...)
        url = f"/images/products/{filename}"
        return jsonify({"ok": True, "url": url})
    except Exception as ex:
        traceback.print_exc()
        return jsonify({"ok": False, "msg": "Upload lỗi", "error": str(ex)}), 500
