# import psycopg2
# import psycopg2.extras
#
# import configure as setting
#
#
# class Db:
#     def __init__(self):
#         self.connection = psycopg2.connect(user=setting.USER,
#                                            password=setting.PASSWORD,
#                                            host=setting.HOST,
#                                            port=setting.PORT,
#                                            database=setting.DB_NAME)
#         self.connection.autocommit = True
#         self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

import sqlite3

conn = sqlite3.connect('bdForJogDir/bdForJob', check_same_thread=False)
cursor = conn.cursor()