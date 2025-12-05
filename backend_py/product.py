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

# DELETE product
@product_bp.delete("/admin/products/<int:id>")
def delete_product(id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM sanphams WHERE id=%s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"msg": "Xóa sản phẩm thành công"})
    except Exception as ex:
        # trả lỗi rõ ràng để frontend hiển thị
        return jsonify({"msg": "Lỗi khi xóa product", "error": str(ex)}), 500

# PUT update product (ví dụ dùng để thay trangThai hoặc cập nhật thông tin)
@product_bp.put("/admin/products/<int:id>")
def update_product(id):
    try:
        d = request.json or {}
        if not d:
            return jsonify({"msg": "Không có dữ liệu cập nhật"}), 400

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
            return jsonify({"msg":"Không có trường hợp lệ để cập nhật"}), 400

        vals.append(id)
        sql = "UPDATE sanphams SET " + ", ".join(fields) + " WHERE id=%s"

        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql, tuple(vals))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"msg":"Cập nhật sản phẩm thành công"})
    except Exception as ex:
        return jsonify({"msg":"Lỗi khi cập nhật product", "error": str(ex)}), 500