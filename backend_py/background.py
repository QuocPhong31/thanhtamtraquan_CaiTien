from flask import Blueprint, request, jsonify, session
from config import get_connection
from werkzeug.utils import secure_filename
import os, time

background_bp = Blueprint("background", __name__)

@background_bp.post("/admin/upload-background")
def upload_background():
    # chỉ admin mới được upload
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    if "image" not in request.files:
        return jsonify({"msg": "Không có file"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"msg": "Tên file rỗng"}), 400

    # thư mục lưu ảnh nền
    upload_dir = os.path.join(os.getcwd(), "image", "background")
    os.makedirs(upload_dir, exist_ok=True)

    # tên file an toàn + không trùng
    filename = secure_filename(file.filename)
    filename = f"bg_{int(time.time())}_{filename}"
    file_path = os.path.join(upload_dir, filename)

    file.save(file_path)

    # đường dẫn public
    db_path = f"/images/background/{filename}"

    # lưu DB
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO anhnens (duongDan, trangThai) VALUES (%s, 'ACTIVE')",
        (db_path,)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "ok": True,
        "url": db_path
    })

@background_bp.get("/admin/api/backgrounds")
def get_backgrounds():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, duongDan, trangThai FROM anhnens ORDER BY id DESC")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@background_bp.put("/admin/backgrounds/<int:id>")
def update_background_status(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.get_json()
    trangThai = data.get("trangThai")

    if trangThai not in ("ACTIVE", "HIDE"):
        return jsonify({"msg": "Trạng thái không hợp lệ"}), 400

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE anhnens SET trangThai=%s WHERE id=%s",
        (trangThai, id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Cập nhật trạng thái thành công"})

@background_bp.delete("/admin/backgrounds/<int:id>")
def delete_background(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM anhnens WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Đã xóa ảnh nền"})
