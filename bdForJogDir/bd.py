import sqlite3 as sq

import parsing as ps
import function as fn

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
                        cost TEXT NOT NULL
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

insertIntoProduct = "INSERT INTO product (id_product, name_product, photo, cost) values(?, ?, ?, ?)"


for item in range(len(ps.countValues)):
    dataProduct = [
    (ps.keysALl[item], ps.infoAll[ps.keysALl[item]]['Название'], fn.photoInsert(ps.infoAll[ps.keysALl[item]]['Фотография']), ps.infoAll[ps.keysALl[item]]['Цена'])
    ]
    with con:
        con.executemany(insertIntoProduct, dataProduct)

# выводим содержимое таблицы на экран
#     with con:
#         data = con.execute("SELECT * FROM product")
#         for row in data:
#             print(row)


# запросы на ввод информации в таблицу пользователей

