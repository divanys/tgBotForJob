CREATE TABLE пользователь (
	ид_п integer PRIMARY KEY AUTOINCREMENT,
	имя string,
	фамилия string,
	номер_карты integer,
	номер_телефона string
);

CREATE TABLE товар (
	ид_т integer PRIMARY KEY AUTOINCREMENT,
	ид_к integer,
	название string,
	стоимость integer,
	фото binary,
	описание text
);

CREATE TABLE заказ (
	ид_з integer PRIMARY KEY AUTOINCREMENT,
	ид_т integer,
	ид_п integer,
	дата date,
	время datetime,
	количество integer
);

CREATE TABLE категория (
	ид_к integer PRIMARY KEY AUTOINCREMENT,
	название_к string
);

CREATE TABLE транзакция (
	ид_тр integer PRIMARY KEY AUTOINCREMENT,
	ид_п integer,
	ид_з integer,
	количество_товаров integer
);






