CREATE TABLE "public.пользователь" (
	"ид_п" serial NOT NULL,
	"имя" VARCHAR(255) NOT NULL,
	"фамилия" VARCHAR(255) NOT NULL,
	"номер_карты" integer NOT NULL,
	"номер_телефона" VARCHAR(255) NOT NULL,
	CONSTRAINT "пользователь_pk" PRIMARY KEY ("ид_п")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.товар" (
	"ид_т" serial NOT NULL,
	"ид_к" integer NOT NULL,
	"название" VARCHAR(255) NOT NULL,
	"стоимость" integer NOT NULL,
	"фото" BINARY NOT NULL,
	"описание" TEXT NOT NULL,
	CONSTRAINT "товар_pk" PRIMARY KEY ("ид_т")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.заказ" (
	"ид_з" serial NOT NULL,
	"ид_т" integer NOT NULL,
	"ид_п" integer NOT NULL,
	"дата" DATE NOT NULL,
	"время" DATETIME NOT NULL,
	"количество" integer NOT NULL,
	CONSTRAINT "заказ_pk" PRIMARY KEY ("ид_з")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.категория" (
	"ид_к" serial NOT NULL,
	"название_к" VARCHAR(255) NOT NULL,
	CONSTRAINT "категория_pk" PRIMARY KEY ("ид_к")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.транзакция" (
	"ид_тр" serial NOT NULL,
	"ид_п" integer NOT NULL,
	"ид_з" integer NOT NULL,
	"количество_товаров" integer NOT NULL,
	CONSTRAINT "транзакция_pk" PRIMARY KEY ("ид_тр")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "товар" ADD CONSTRAINT "товар_fk0" FOREIGN KEY ("ид_к") REFERENCES "категория"("ид_к");

ALTER TABLE "заказ" ADD CONSTRAINT "заказ_fk0" FOREIGN KEY ("ид_т") REFERENCES "товар"("ид_т");
ALTER TABLE "заказ" ADD CONSTRAINT "заказ_fk1" FOREIGN KEY ("ид_п") REFERENCES "пользователь"("ид_п");


ALTER TABLE "транзакция" ADD CONSTRAINT "транзакция_fk0" FOREIGN KEY ("ид_п") REFERENCES "пользователь"("ид_п");
ALTER TABLE "транзакция" ADD CONSTRAINT "транзакция_fk1" FOREIGN KEY ("ид_з") REFERENCES "заказ"("ид_з");






