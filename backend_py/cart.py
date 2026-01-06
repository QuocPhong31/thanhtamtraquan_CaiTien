from flask import Blueprint, request, session, jsonify
from config import get_connection

cart_bp = Blueprint("cart", __name__)

def get_cart():
    return session.get("cart", [])

def save_cart(cart):
    session["cart"] = cart
    session.modified = True

@cart_bp.post("/api/cart/add")
def add_to_cart():
    data = request.json
    if not data:
        return jsonify({"msg": "Thiếu dữ liệu"}), 400

    product_id = data.get("id")
    name = data.get("name")
    price = data.get("price")
    image = data.get("image")
    qty = int(data.get("qty", 1))
    ptype = data.get("type", "tea")

    if not product_id or qty < 1:
        return jsonify({"msg": "Dữ liệu không hợp lệ"}), 400

    cart = get_cart()

    # kiểm tra sản phẩm đã tồn tại
    for item in cart:
        if item["id"] == product_id and item["type"] == ptype:
            item["qty"] += qty
            save_cart(cart)
            return jsonify({"cart": cart})

    # chưa có → thêm mới
    cart.append({
        "id": product_id,
        "type": ptype,
        "name": name,
        "price": price,
        "image": image,
        "qty": qty
    })

    save_cart(cart)
    return jsonify({"cart": cart})

@cart_bp.post("/api/cart/remove")
def remove_item():
    data = request.json
    index = data.get("index")

    cart = get_cart()

    if index is None or index < 0 or index >= len(cart):
        return jsonify({"msg": "Index không hợp lệ"}), 400

    cart.pop(index)
    save_cart(cart)

    return jsonify(cart)

# @cart_bp.get("/api/cart")
# def get_cart_api():
#     return jsonify(get_cart())


# @cart_bp.post("/api/order/create")
# def create_order():
#     data = request.json
#
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("""
#       INSERT INTO orders (order_code, amount, payment_method, status)
#       VALUES (%s, %s, %s, 'WAITING_CONFIRM')
#     """, (
#       data["order_code"],
#       data["amount"],
#       data["method"]
#     ))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     return {"ok": True}
