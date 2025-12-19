from flask import Blueprint, jsonify
from config import get_connection

public_bp = Blueprint("public", __name__)

@public_bp.get("/api/products")
def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sanphams")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

@public_bp.get("/api/products/<int:id>")
def get_product(id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, tenSanPham, gia, khoiLuongHop, soLuong, xuatXu, moTa, huongVi, congDung, cachPha, anh, trangThai FROM sanphams WHERE id=%s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        return jsonify({"msg": "Không tìm thấy sản phẩm"}), 404

    # map fields sang tên dùng ở frontend
    product = {
        "id": row["id"],
        "title": row.get("tenSanPham"),
        "price": row.get("gia"),
        "khoiLuongHop": row.get("khoiLuongHop"),
        "soLuong": row.get("soLuong"),
        "xuatXu": row.get("xuatXu"),
        "description": row.get("moTa"),
        # 'anh' ở DB lưu dạng '/images/products/xxx.jpg' -> trả thành image
        "huongVi": row.get("huongVi"),
        "congDung": row.get("congDung"),
        "cachPha": row.get("cachPha"),
        "image": row.get("anh") or "",
        "trangThai": row.get("trangThai")
    }
    return jsonify(product)

@public_bp.get("/api/backgrounds")
def get_backgrounds():
    """
    Lấy danh sách ảnh nền đang ACTIVE
    DB lưu đường dẫn dạng: /images/background/xxx.jpg
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, duongDan
        FROM anhnens
        WHERE trangThai = 'ACTIVE'
        ORDER BY ngayTao DESC
    """)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)