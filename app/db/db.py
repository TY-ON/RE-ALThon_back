import sqlite3


def get_data(board):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {board}")
    rows = cur.fetchall()
    return rows, conn, cur
    
def close_db(conn):
    conn.commit()
    conn.close()

def search_user(id, pw):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT username FROM user_data WHERE id=? AND password=?", (id, pw))
    rows = cur.fetchall()
    conn.close()
    if len(rows) != 1:
        return False
    return rows[0][0]
    
def insert_user(id, pw, username):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT username FROM user_data WHERE id=? OR username=?", (id, username))
    search_name = cur.fetchall()
    
    if search_name: # if exists
        conn.close()
        return False
    cur.execute("INSERT INTO user_data values (?, ?, ?)", (id, pw, username))
    conn.commit()
    conn.close()
    return username

def delete_user(id, pw):
    username = search_user(id, pw)
    if username: # if exists
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM user_dasa WHERE username=? AND id=? AND password=?", (username, id, pw))
        conn.commit()
        conn.close()
    return username
    
def get_data_from_name(username):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT username FROM user_data WHERE name=?", (username))
    rows = cur.fetchall()
    conn.close()
    if len(rows) != 1:
        return False
    return rows[0][0]