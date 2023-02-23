import sqlite3 as sq

# from parsingDir import parsing as ps


con = sq.connect('bdForJogDir/dataBase.db')

with con:
    # получаем количество таблиц с нужным нам именем
    data = con.execute("select count(*) from sqlite_master where type='table' and name='product'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
            
            # создаём таблицу для товаров
            with con:
                con.execute("""
                    CREATE TABLE IF NOT EXISTS product (
                        id_product INT PRIMARY KEY NOT NULL,
                        name_product TEXT NOT NULL,
                        photo BLOB NOT NULL,
                        cost INTEGER NOT NULL
                    );
                """)

with con:
    # получаем количество таблиц с нужным нам именем
    data = con.execute("select count(*) from sqlite_master where type='table' and name='users'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
            
            # создаём таблицу для товаров
            with con:
                con.execute("""
                    CREATE TABLE IF NOT EXISTS product (
                        id_user INT PRIMARY KEY NOT NULL,
                        role 
                    );
                """)