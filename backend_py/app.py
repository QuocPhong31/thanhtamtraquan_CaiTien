from flask import Flask, send_from_directory, render_template, redirect, session
from flask_cors import CORS

from routes_public import public_bp
from admin import admin_bp
from user import user_bp
from product import product_bp
from teapot import teapot_bp
from background import background_bp
from contact import contact_bp
import os

app = Flask(__name__)
app.secret_key = "thanh_tam_tra_quan_secret_key"

CORS(
    app,
    supports_credentials=True,
    resources={
        r"/api/*": {
            "origins": [
                "https://quocphong31.github.io",
                "https://shop.thanhtamtraquan.com",
                "http://127.0.0.1:5500",
                "http://localhost:5500"
            ]
        }
    }
)

# Đường dẫn tới thư mục chứa frontend
STATIC_DIR = os.path.join(os.path.dirname(__file__), "web")

# API cho user (bạn đang dùng)
app.register_blueprint(public_bp)

# Admin routes
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)
app.register_blueprint(teapot_bp)
app.register_blueprint(background_bp)
app.register_blueprint(contact_bp)

@app.get("/")
def home():
    return "API chạy OK + Admin OK"

# Khi truy cập /admin/ cần phải có session admin, nếu chưa => redirect /admin/login
@app.get("/admin/")
def admin_page():
    if not session.get("admin"):
        return redirect("/admin/login")
    # truyền admin từ session vào template (để Jinja có biến admin)
    return render_template("admin/index.html", admin=session.get("admin"))

@app.route('/images/<path:filename>')
def serve_image(filename):
    # image dir là backend_py/image
    image_dir = os.path.join(app.root_path, 'image')
    return send_from_directory(image_dir, filename)

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
