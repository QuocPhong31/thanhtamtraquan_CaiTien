from flask import Blueprint, request, jsonify
from config import get_connection

product_bp = Blueprint("products_admin", __name__)

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
        d["tenSanPham"], d["gia"], d["moTa"], d["anh"],
        d["soLuong"], d["trangThai"]
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"msg": "Tạo sản phẩm thành công"})
