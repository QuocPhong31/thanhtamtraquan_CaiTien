from datetime import datetime
from flask import Blueprint, jsonify, session
from config import get_connection

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