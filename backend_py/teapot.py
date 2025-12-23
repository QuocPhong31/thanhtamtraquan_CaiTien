from flask import Blueprint, request, jsonify
from config import get_connection
import os, time, uuid, traceback
from werkzeug.utils import secure_filename

teapot_bp = Blueprint("teapots_admin", __name__)


BASE_DIR = os.path.dirname(__file__)
UPLOAD_ROOT = os.path.join(BASE_DIR, "image", "teapots")
os.makedirs(UPLOAD_ROOT, exist_ok=True)

ALLOWED_EXT = {"png", "jpg", "jpeg", "gif", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT

@teapot_bp.get("/admin/teapots")
def admin_get_teapots():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM amtras")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@teapot_bp.post("/admin/teapots")
def admin_add_teapot():
    d = request.json
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO amtras
        (tenAmTra, gia, soLuong, xuatXu, moTa, chatLieu, thietKe, cachSuDung, anh, trangThai)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        d.get("tenAmTra"),
        d.get("gia"),
        d.get("soLuong"),
        d.get("xuatXu"),
        d.get("moTa"),
        d.get("chatLieu"),
        d.get("thietKe"),
        d.get("cachSuDung"),
        d.get("anh"),
        d.get("trangThai") or "ACTIVE"
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Thêm ấm trà thành công"})


@teapot_bp.put("/admin/teapots/<int:id>")
def update_teapot(id):
    d = request.json
    fields, vals = [], []

    mapping = {
        "tenAmTra": "tenAmTra",
        "gia": "gia",
        "soLuong": "soLuong",
        "xuatXu": "xuatXu",
        "moTa": "moTa",
        "chatLieu": "chatLieu",
        "thietKe": "thietKe",
        "cachSuDung": "cachSuDung",
        "anh": "anh",
        "trangThai": "trangThai"
    }

    for k, col in mapping.items():
        if k in d:
            fields.append(f"{col}=%s")
            vals.append(d[k])

    if not fields:
        return jsonify({"msg": "Không có dữ liệu cập nhật"}), 400

    vals.append(id)
    sql = "UPDATE amtras SET " + ", ".join(fields) + " WHERE id=%s"

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql, tuple(vals))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Cập nhật ấm trà thành công"})


@teapot_bp.delete("/admin/teapots/<int:id>")
def delete_teapot(id):
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute("SELECT anh FROM amtras WHERE id=%s", (id,))
        row = cur.fetchone()

        if row and row.get("anh"):
            rel = row["anh"].replace("/images/", "").replace("/", os.sep)
            file_path = os.path.join(BASE_DIR, "image", rel)
            if os.path.exists(file_path):
                os.remove(file_path)

        cur.execute("DELETE FROM amtras WHERE id=%s", (id,))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"msg": "Đã xóa ấm trà"})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"msg": "Lỗi xóa ấm trà"}), 500


@teapot_bp.post("/admin/upload-teapot-image")
def upload_teapot_image():
    if "image" not in request.files:
        return jsonify({"ok": False}), 400

    file = request.files["image"]
    if not allowed_file(file.filename):
        return jsonify({"ok": False}), 400

    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)
    filename = f"{name}_{int(time.time())}_{uuid.uuid4().hex[:6]}{ext}"

    save_path = os.path.join(UPLOAD_ROOT, filename)
    file.save(save_path)

    return jsonify({
        "ok": True,
        "url": f"/images/teapots/{filename}"
    })
