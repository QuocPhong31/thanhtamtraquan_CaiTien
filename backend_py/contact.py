from flask import Blueprint, request, jsonify, session
from config import get_connection

contact_bp = Blueprint("contact", __name__)

# ===================== ADDRESS =====================

@contact_bp.get("/admin/address")
def get_address():
    # chỉ admin
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM address_contact ORDER BY ngayTao DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)


@contact_bp.post("/admin/address")
def add_address():
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    noiDung = data.get("noiDung")

    if not noiDung:
        return jsonify({"msg": "Thiếu nội dung address"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO address_contact (noiDung, trangThai) VALUES (%s, 'ACTIVE')",
        (noiDung,)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã thêm address"})


@contact_bp.put("/admin/address/<int:id>")
def update_address(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    trangThai = data.get("trangThai")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE address_contact SET trangThai=%s WHERE id=%s",
        (trangThai, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã cập nhật address"})

@contact_bp.put("/admin/address/edit/<int:id>")
def edit_address(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    noiDung = data.get("noiDung")

    if not noiDung:
        return jsonify({"msg": "Thiếu nội dung"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE address_contact SET noiDung=%s WHERE id=%s",
        (noiDung, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã sửa address"})

# ===================== EMAIL =====================

@contact_bp.get("/admin/email")
def get_email():
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM email_contact ORDER BY ngayTao DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)


@contact_bp.post("/admin/email")
def add_email():
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    noiDung = data.get("noiDung")

    if not noiDung:
        return jsonify({"msg": "Thiếu nội dung email"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO email_contact (noiDung, trangThai) VALUES (%s, 'ACTIVE')",
        (noiDung,)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã thêm email"})


@contact_bp.put("/admin/email/<int:id>")
def update_email(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    trangThai = data.get("trangThai")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE email_contact SET trangThai=%s WHERE id=%s",
        (trangThai, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã cập nhật email"})

@contact_bp.put("/admin/email/edit/<int:id>")
def edit_email(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    noiDung = data.get("noiDung")

    if not noiDung:
        return jsonify({"msg": "Thiếu nội dung"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE email_contact SET noiDung=%s WHERE id=%s",
        (noiDung, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã sửa email"})

# ===================== PHONE =====================

@contact_bp.get("/admin/phone")
def get_phone():
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM phone_contact ORDER BY ngayTao DESC")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)


@contact_bp.post("/admin/phone")
def add_phone():
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    noiDung = data.get("noiDung")

    if not noiDung:
        return jsonify({"msg": "Thiếu nội dung phone"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO phone_contact (noiDung, trangThai) VALUES (%s, 'ACTIVE')",
        (noiDung,)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã thêm phone"})


@contact_bp.put("/admin/phone/<int:id>")
def update_phone(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    trangThai = data.get("trangThai")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE phone_contact SET trangThai=%s WHERE id=%s",
        (trangThai, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã cập nhật phone"})

@contact_bp.put("/admin/phone/edit/<int:id>")
def edit_phone(id):
    if not session.get("admin"):
        return jsonify({"msg": "Unauthorized"}), 401

    data = request.json
    noiDung = data.get("noiDung")

    if not noiDung:
        return jsonify({"msg": "Thiếu nội dung"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE phone_contact SET noiDung=%s WHERE id=%s",
        (noiDung, id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"msg": "Đã sửa phone"})
