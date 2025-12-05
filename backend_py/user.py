from flask import Blueprint, request, jsonify
from config import get_connection
from utils import hash_password

user_bp = Blueprint("users", __name__)

# Lấy danh sách user
@user_bp.get("/admin/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM nguoidungs")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

# Tạo user mới
@user_bp.post("/admin/users")
def create_user():
    d = request.json

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO nguoidungs (hoTen, gioiTinh, ngaySinh, diaChi, SDT, email, taiKhoan, matKhau, role)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        d["hoTen"], d["gioiTinh"], d["ngaySinh"], d["diaChi"], d["SDT"], d["email"],
        d["taiKhoan"], hash_password(d["matKhau"]), d.get("role", "USER")
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Tạo user thành công"})
