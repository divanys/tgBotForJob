import sqlite3

conn = sqlite3.connect('bdForJobs.db', check_same_thread=False)
cursor = conn.cursor()
conn.close()