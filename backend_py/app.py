from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from config import get_connection
import os

app = Flask(__name__)
CORS(app)

# Đường dẫn tới thư mục chứa frontend
STATIC_DIR = os.path.join(os.path.dirname(__file__), "web")

@app.route("/api/products")
def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route("/api/products/<int:id>")
def get_product(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    p = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(p)

# Serve index.html
@app.route("/")
def home():
    return "API chạy OK"

# Serve trang product (1 file dùng chung)
@app.route("/product/<int:id>")
def product_page(id):
    return send_from_directory(os.path.join(STATIC_DIR, "Product"), "product.html")

# Serve tất cả file tĩnh còn lại (CSS, JS, images,...)
@app.route("/<path:path>")
def static_proxy(path):
    return send_from_directory(STATIC_DIR, path)

if __name__ == "__main__":
    app.run(debug=True)
