from flask import Blueprint, request, jsonify, session
from config import get_connection
import os, time
from werkzeug.utils import secure_filename

payment_bp = Blueprint("payment", __name__)

UPLOAD_DIR = os.path.join(os.getcwd(), "image", "payment")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@payment_bp.get("/admin/api/payments")
def get_payments():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM taikhoan_thanhtoan ORDER BY id DESC")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@payment_bp.get("/admin/api/orders")
def get_orders():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT
            id, hoTen, sdt, email, diaChi,
            tenSanPham, soLuong, thongTinCK,
            soTien, trangThai, ngayTao
        FROM donthanhtoan
        ORDER BY ngayTao DESC
    """)
    data = cur.fetchall()

    cur.close()
    conn.close()
    return jsonify(data)

@payment_bp.post("/admin/upload-payment")
def upload_payment():
    if "image" not in request.files:
        return {"msg": "Thiếu ảnh QR"}, 400

    file = request.files["image"]
    nganHang = request.form.get("nganHang")
    soTaiKhoan = request.form.get("soTaiKhoan")
    chuTaiKhoan = request.form.get("chuTaiKhoan")

    if not all([nganHang, soTaiKhoan, chuTaiKhoan]):
        return {"msg": "Thiếu thông tin"}, 400

    filename = secure_filename(file.filename)
    filename = f"qr_{int(time.time())}_{filename}"
    file.save(os.path.join(UPLOAD_DIR, filename))

    db_path = f"/images/payment/{filename}"

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
      INSERT INTO taikhoan_thanhtoan
      (nganHang, soTaiKhoan, chuTaiKhoan, anhQR)
      VALUES (%s,%s,%s,%s)
    """, (nganHang, soTaiKhoan, chuTaiKhoan, db_path))
    conn.commit()
    cur.close()
    conn.close()

    return {"ok": True}

@payment_bp.put("/admin/payments/<int:id>")
def toggle_payment(id):
    status = request.json.get("trangThai")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE taikhoan_thanhtoan SET trangThai=%s WHERE id=%s",
        (status, id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return {"ok": True}

@payment_bp.delete("/admin/payments/<int:id>")
def delete_payment(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM taikhoan_thanhtoan WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"ok": True}

@payment_bp.put("/admin/orders/<int:id>")
def update_order_status(id):
    status = request.json.get("trangThai")
    if status not in ["daXacNhan", "huyXacNhan"]:
        return {"msg": "Trạng thái không hợp lệ"}, 400

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE donthanhtoan SET trangThai=%s WHERE id=%s",
        (status, id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return {"ok": True}

@payment_bp.get("/api/payments/active")
def get_active_payment():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT id, nganHang, soTaiKhoan, chuTaiKhoan, anhQR
        FROM taikhoan_thanhtoan
        WHERE trangThai = 'ACTIVE'
        ORDER BY id DESC
        LIMIT 1
    """)
    row = cur.fetchone()

    cur.close()
    conn.close()

    if not row:
        return jsonify({"msg": "Chưa có tài khoản thanh toán"}), 404

    return jsonify(row)

@payment_bp.post("/api/order/create")
def create_order():
    data = request.get_json()

    required = ["hoTen", "sdt", "diaChi", "thongTinCK", "amount", "tenSanPham", "soLuong"]
    for f in required:
        if not data.get(f):
            return {"msg": f"Thiếu trường {f}"}, 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
      INSERT INTO donthanhtoan
      (hoTen, sdt, email, diaChi, thongTinCK, soTien, tenSanPham, soLuong)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
      data["hoTen"],
      data["sdt"],
      data.get("email"),
      data["diaChi"],
      data["thongTinCK"],
      data["amount"],
      data["tenSanPham"],
      data["soLuong"]
    ))

    conn.commit()
    cur.close()
    conn.close()

    return {"ok": True}