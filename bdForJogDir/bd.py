import sqlite3

conn = sqlite3.connect('server.db', check_same_thread=False)
cursor = conn.cursor()
conn.close()