import sqlite3

conn = sqlite3.connect("database.db")
#conn.execute(f"DROP TABLE board")
conn.execute("""CREATE TABLE user_data (
    userNum INTEGER PRIMARY KEY autoincrement,
    id text, 
    password text, 
    username text);""")

conn.execute("""CREATE TABLE product (
    prodNum INTEGER PRIMARY KEY autoincrement,
    name text, 
    kind text, 
    price text,
    content text,
    image text,
    useyn DEFAULT "y"
    regdate DATE, 
    prodSeq);""")
data = []
for i in data:
    
