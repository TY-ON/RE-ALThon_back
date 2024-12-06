import sqlite3

def get_list(category=False):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    if not category:
        cur.execute(f"SELECT name, company, score, price, image FROM product LIMIT 9")
    else:
        return False
    rows = cur.fetchall()
    conn.close()
    return rows