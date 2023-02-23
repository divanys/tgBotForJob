import sqlite3 as sq

# from parsingDir import parsing as ps


con = sq.connect('bdForJogDir/dataBase.db')


'''
Блок создания таблиц 
'''


with con:
    data = con.execute("select count(*) from sqlite_master where type='table' and name='product'")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                    CREATE TABLE IF NOT EXISTS product (
                        id_product INT PRIMARY KEY NOT NULL,
                        name_product TEXT NOT NULL,
                        photo BLOB NOT NULL,
                        cost INTEGER NOT NULL
                    );
                """)

    data = con.execute("select count(*) from sqlite_master where type='table' and name='users'")
    for row in data:
        if row[0] == 0:         
            with con:
                con.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id_user INT PRIMARY KEY NOT NULL,
                        role TEXT NOT NULL,
                        fname TEXT,
                        lname TEXT
                    );
                """)

    data = con.execute("select count(*) from sqlite_master where type='table' and name='category'")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                    CREATE TABLE IF NOT EXISTS category (
                        id_category INT PRIMARY KEY NOT NULL,
                        name_category TEXT NOT NULL
                    );
                """)

#     data = con.execute("select count(*) from sqlite_master where type='table' and name='order'")
#     for row in data:
#         if row[0] == 0:
#             with con:
#                 con.execute("""
#                     CREATE TABLE IF NOT EXISTS order (
#                         id_category INT PRIMARY KEY NOT NULL AUTOINCREMENT,
#                         name_category TEXT NOT NULL
#                     );
#                 """)

#     data = con.execute("select count(*) from sqlite_master where type='table' and name='transaction'")
#     for row in data:
#         if row[0] == 0:
#             with con:
#                 con.execute("""
#                     CREATE TABLE IF NOT EXISTS transaction (
#                         id_category INT PRIMARY KEY NOT NULL AUTOINCREMENT,
#                         name_category TEXT NOT NULL
#                     );
#                 """)


'''
Блок заполнения таблиц
'''


