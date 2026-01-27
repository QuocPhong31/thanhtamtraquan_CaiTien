from flask import Blueprint, request, jsonify
from config import get_connection
import traceback

stock_bp = Blueprint("stock_admin", __name__)

@stock_bp.post("/admin/stock")
def handle_stock():
    try:
        d = request.json
        sanPhamId = d.get("sanPhamId")
        soLuong = int(d.get("soLuong"))
        loai = d.get("loai")  # NHAP / DIEU_CHINH / TRA_HANG

        if not sanPhamId or not loai:
            return jsonify({"msg": "Thiếu dữ liệu"}), 400

        if soLuong < 0:
            return jsonify({"msg": "Số lượng không hợp lệ"}), 400

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute("SELECT soLuong FROM sanphams WHERE id=%s", (sanPhamId,))
        row = cur.fetchone()
        if not row:
            return jsonify({"msg": "Không tìm thấy sản phẩm"}), 404

        current = row["soLuong"]

        if loai == "NHAP":
            new_qty = current + soLuong

        elif loai == "TRA_HANG":
            if soLuong > current:
                return jsonify({"msg": "Trả hàng vượt quá tồn kho"}), 400
            new_qty = current - soLuong

        elif loai == "DIEU_CHINH":
            new_qty = soLuong  # SET TRỰC TIẾP

        else:
            return jsonify({"msg": "Loại không hợp lệ"}), 400

        if new_qty < 0:
            return jsonify({"msg": "Số lượng không hợp lệ"}), 400

        cur.execute(
            "UPDATE sanphams SET soLuong=%s WHERE id=%s",
            (new_qty, sanPhamId)
        )

        cur.execute("""
          INSERT INTO nhapKhoSanPhams (sanPhamId, soLuong, loai, nguoiThucHien)
          VALUES (%s,%s,%s,%s)
        """, (
            sanPhamId,
            soLuong,
            loai,
            1
        ))

        conn.commit()
        return jsonify({"msg": "OK"})

    except Exception as ex:
        traceback.print_exc()
        return jsonify({"msg": "Lỗi nhập kho", "error": str(ex)}), 500


@stock_bp.post("/admin/stock/teapot")
def handle_stock_teapot():
    try:
        d = request.json
        amTraId = d.get("amTraId")
        soLuong = int(d.get("soLuong"))
        loai = d.get("loai")

        if not amTraId or not loai:
            return jsonify({"msg": "Thiếu dữ liệu"}), 400

        if soLuong < 0:
            return jsonify({"msg": "Số lượng không hợp lệ"}), 400

        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        cur.execute("SELECT soLuong FROM amtras WHERE id=%s", (amTraId,))
        row = cur.fetchone()
        if not row:
            return jsonify({"msg": "Không tìm thấy ấm trà"}), 404

        current = row["soLuong"]

        if loai == "NHAP":
            new_qty = current + soLuong

        elif loai == "TRA_HANG":
            if soLuong > current:
                return jsonify({"msg": "Trả hàng vượt tồn kho"}), 400
            new_qty = current - soLuong

        elif loai == "DIEU_CHINH":
            new_qty = soLuong

        else:
            return jsonify({"msg": "Loại không hợp lệ"}), 400

        cur.execute(
            "UPDATE amtras SET soLuong=%s WHERE id=%s",
            (new_qty, amTraId)
        )

        cur.execute("""
          INSERT INTO nhapKhoAmTras (amTraId, soLuong, loai, nguoiThucHien)
          VALUES (%s,%s,%s,%s)
        """, (amTraId, soLuong, loai, 1))

        conn.commit()
        return jsonify({"msg": "OK"})

    except Exception as ex:
        traceback.print_exc()
        return jsonify({"msg": "Lỗi nhập kho ấm trà", "error": str(ex)}), 500
