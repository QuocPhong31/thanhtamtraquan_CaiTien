from datetime import datetime
from flask import Blueprint, jsonify, request
from config import get_connection
from datetime import datetime

stats_bp = Blueprint("stats", __name__)

@stats_bp.get("/admin/stats/summary/daily")
def summary_daily():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*) 
        FROM truycap_logs
        WHERE DATE(visited_at) = CURDATE()
    """)
    total = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"total": total})

@stats_bp.get("/admin/stats/summary/monthly")
def summary_monthly():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            MONTH(CURDATE()) AS month,
            YEAR(CURDATE()) AS year,
            IFNULL(SUM(total), 0) AS total
        FROM luottruycap_ngay
        WHERE YEAR(date)=YEAR(CURDATE())
          AND MONTH(date)=MONTH(CURDATE())
    """)
    row = cur.fetchone()
    cur.close()
    conn.close()

    return jsonify({
        "month": row[0],
        "year": row[1],
        "total": row[2]
    })

@stats_bp.get("/admin/stats/summary/yearly")
def summary_yearly():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT IFNULL(SUM(total), 0)
        FROM luottruycap_ngay
        WHERE YEAR(date) >= 2025
    """)
    total = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({
        "from": 2025,
        "to": datetime.now().year,
        "total": total
    })

@stats_bp.get("/admin/stats/revenue")
def stats_revenue():
    mode = request.args.get("mode", "month")
    year = int(request.args.get("year", datetime.now().year))
    month = request.args.get("month", type=int)
    quarter = request.args.get("quarter", type=int)

    conn = get_connection()
    cur = conn.cursor()

    base_where = "YEAR(ngayTao) = %s"
    params = [year]

    if mode == "month" and month:
        base_where += " AND MONTH(ngayTao) = %s"
        params.append(month)

    elif mode == "quarter" and quarter:
        base_where += " AND QUARTER(ngayTao) = %s"
        params.append(quarter)

    sql = f"""
        SELECT
          COUNT(*) AS total_orders,
          SUM(CASE WHEN trangThai = 'daXacNhan' THEN 1 ELSE 0 END) AS confirmed_orders,
          IFNULL(SUM(CASE WHEN trangThai = 'daXacNhan' THEN soTien ELSE 0 END), 0) AS revenue
        FROM donthanhtoan
        WHERE {base_where}
    """

    cur.execute(sql, params)
    row = cur.fetchone()
    cur.close()
    conn.close()

    return jsonify({
        "booking": row[0] or 0,
        "confirmed": row[1] or 0,
        "revenue": int(row[2] or 0)
    })
