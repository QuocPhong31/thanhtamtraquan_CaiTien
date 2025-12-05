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
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sanphams WHERE id=%s", (id,))
    p = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(p)
