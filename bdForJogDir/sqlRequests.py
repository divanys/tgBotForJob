
import bd 
# import tg 
sql = bd.con.cursor()

# запросы на ввод информации в таблицу пользователей

# insertUsers = "INSERT INTO users (id_user, role, fname, lname) values(?, ?, ?, ?)"

def start(idu, role, fname, lname):
    sql.execute(f"SELECT id_user FROM users WHERE id_user = {idu}")
    sql.execute(f"INSERT INTO users VALUES ({idu}, {role}, {fname}, {lname})")
	

# def start(message):
#     try:
#         getname = message.from_user.first_name
#         cid = message.chat.id
#         uid = message.from_user.id
        
# 		# sql.execute(f"SELECT id FROM users WHERE id = {uid}") 
#         user = sql.start(idu=uid)

#         if user.fetchone() is None:
# 			#sql.execute(f"INSERT INTO users VALUES ({uid}, '{getname}', 0, 0, 0)")
# 			#db.commit()
#             sql.start(idu=uid, role='0', fname=getname, lname='000')
#             dp.send_message(cid, "Добро Пожаловать")
#         else:
#             dp.send_message(cid, f"зареган")
#     except:
#         dp.send_message(cid, f'🚫 | Ошибка при выполнении команды')
