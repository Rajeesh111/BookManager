import sqlite3


def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS book(
             id INTEGER PRIMARY KEY,
             title TEXT,
             author TEXT,
             year INTEGER,
             genre TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert(title,author,year,genre):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,genre))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",genre=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()

    query = "SELECT * FROM book WHERE 1=1"
    params = []

    if title:
        query=query+ " AND title LIKE ?"
        params.append(f"%{title}%")

    if author:
        query = query + " AND author LIKE ?"
        params.append(f"%{author}%")

    if year:
        query = query + " AND year=?"
        params.append(year)

    if genre:
        query += " AND genre LIKE ?"
        params.append(f"%{genre}%")

    cur.execute(query,params)
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,genre):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?,genre=? WHERE id=?",(title,author,year,genre,id))
    conn.commit()
    conn.close()





















