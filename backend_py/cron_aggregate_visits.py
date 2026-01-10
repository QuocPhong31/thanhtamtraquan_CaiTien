from config import get_connection
from datetime import datetime, timedelta
import pytz

def rollup_daily_logs():
    conn = get_connection()
    cur = conn.cursor()

    VN_TZ = pytz.timezone("Asia/Ho_Chi_Minh")
    now_vn = datetime.now(VN_TZ)
    yesterday = (now_vn - timedelta(days=1)).date()
    # 1. check đã rollup hôm qua chưa
    cur.execute(
        "SELECT 1 FROM rollup_log WHERE date=%s",
        (yesterday,)
    )
    if cur.fetchone():
        cur.close()
        conn.close()
        return

    # 2. tổng hợp lượt truy cập hôm qua
    cur.execute("""
            INSERT INTO luottruycap_ngay (date, total)
            SELECT %s, COUNT(*)
            FROM truycap_logs
            WHERE DATE(visited_at) = %s
            ON DUPLICATE KEY UPDATE total=VALUES(total)
        """, (yesterday, yesterday))

    # 3. xóa log cũ hơn hôm qua
    cur.execute("""
            DELETE FROM truycap_logs
            WHERE DATE(visited_at) < %s
        """, (yesterday,))

    # 4. đánh dấu đã rollup
    cur.execute(
        "INSERT INTO rollup_log (date) VALUES (%s)",
        (yesterday,)
    )

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

if __name__ == "__main__":
    rollup_daily_logs()