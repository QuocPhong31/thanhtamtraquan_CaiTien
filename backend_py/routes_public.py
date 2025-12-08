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
    cur.execute("SELECT id, tenSanPham, gia, moTa, anh, soLuong, trangThai FROM sanphams WHERE id=%s", (id,))
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
        "description": row.get("moTa"),
        # 'anh' ở DB lưu dạng '/images/products/xxx.jpg' -> trả thành image
        "image": row.get("anh") or "",
        "soLuong": row.get("soLuong"),
        "trangThai": row.get("trangThai")
    }
    return jsonify(product)
