from config import get_connection

def rollup_daily_logs():
    conn = get_connection()
    cur = conn.cursor()

    # 1️. kiểm tra hôm qua đã rollup chưa
    cur.execute("""
        SELECT 1 FROM rollup_log
        WHERE date = CURDATE()  
    """)
    existed = cur.fetchone()

    if not existed:
        # 2️. tổng kết hôm qua
        cur.execute("""
            INSERT INTO luottruycap_ngay (date, total)
            SELECT
              CURDATE() - INTERVAL 1 DAY,
              COUNT(*)
            FROM truycap_logs
            WHERE visited_at >= DATE_SUB(CURDATE(), INTERVAL 1 DAY)
              AND visited_at < CURDATE()
            ON DUPLICATE KEY UPDATE
              total = VALUES(total);
        """)

        # 3️. xóa log cũ
        cur.execute("""
            DELETE FROM truycap_logs
            WHERE DATE(visited_at) < CURDATE()
        """)

        # 4️. đánh dấu đã rollup
        cur.execute("""
            INSERT INTO rollup_log (date)
            VALUES (CURDATE() - INTERVAL 1 DAY)
        """)

    # 5️. CHỈ GIỮ 5 NGÀY GẦN NHẤT
    cur.execute("""
        DELETE FROM rollup_log
        WHERE date < (
            SELECT date FROM (
                SELECT date
                FROM rollup_log
                ORDER BY date DESC
                LIMIT 1 OFFSET 4
            ) AS t
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
