#Taller conexion con base de datos
#Estudiante: Santiago Hernandez Molina
#Codigo: 2280552
#fecha: 11-09-2021

import psycopg2
import json
from random import randrange
from datetime import timedelta
from datetime import datetime


def insert_json_characters(lista):
    for diccionario in lista:
        bd.insertar_personajes(diccionario["cit_id"], diccionario["uni_id"],
                               diccionario["name"], diccionario["path"], diccionario["description"])


def insert_json_powers(lista):
    for diccionario in lista:
        bd.insertar_poderes(diccionario["name"])


def insert_json_powers_character(lista):
    for diccionario in lista:
        bd.insert_powers_character(diccionario["pow_id"], diccionario["cha_id"],
                               diccionario["level"])


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def update_dates_random(bd):
    contador = 1
    personajes = bd.lista_personajes()
    for personaje in personajes:
        try:
            d1 = datetime.strptime('1/1/2005', '%m/%d/%Y')
            d2 = datetime.strptime('1/1/2021', '%m/%d/%Y')
            date = random_date(d1, d2)
            bd.update_birthdate(contador, date)
            contador += 1
        except Exception as e:
            break


def characters_archive():
    with open("database/characters.txt", mode="r", encoding="utf-8") as archivo:
        personajes = (archivo.read())
        lista_pj = json.loads(personajes)
        return lista_pj


def powers_archive():
    with open("database/powers.txt", mode="r", encoding="utf-8") as archivo:
        powers = (archivo.read())
        lista_powers = json.loads(powers)
        return lista_powers


def powers_character_archive():
    with open("database/powers_character.txt", mode="r", encoding="utf-8") as archivo:
        powers_character = (archivo.read())
        lista_pc = json.loads(powers_character)
        return lista_pc


class Database:

    def __init__(self):
        self.conection = psycopg2.connect(
            host='localhost',
            database='db_narvel',
            user='postgres',
            password=''

        )

        self.cursor = self.conection.cursor()
        print('conexion exitosa')

    def lista_personajes(self):
        sql = "select id, name, description, uni_id from characters"
        try:
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            return lista
        except Exception as e:
            raise

    def lista_poderes(self):
        sql = "select * from powers"
        try:
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            return lista
        except Exception as e:
            raise

    def consultas_sql(self, sql):
        try:
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            return lista
        except Exception as e:
            raise

    def insertar_poderes(self, power):
        sql = "INSERT INTO public.powers (name) VALUES (%s);"
        try:
            self.cursor.execute(sql, (power,))
            self.conection.commit()

        except Exception as e:
            print(e)

    def insertar_personajes(self, cit_id, uni_id, name, path, description):
        sql = "INSERT INTO public.characters (cit_id, uni_id, name, path, description) VALUES (%s,%s,%s,%s,%s);"
        try:
            self.cursor.execute(sql, (cit_id, uni_id, name, path, description))
            self.conection.commit()

        except Exception as e:
            print(e)

    def insert_powers_character(self, pow_id, cha_id, level):
        sql = "INSERT INTO public.powers_character (pow_id, cha_id, level) VALUES (%s,%s,%s);"
        try:
            self.cursor.execute(sql, (pow_id, cha_id, level))
            self.conection.commit()

        except Exception as e:
            print(e)

    def add_column_birthdate(self):
        sql = "alter table characters add birthdate date;"
        try:
            self.cursor.execute(sql)
            self.conection.commit()
        except Exception as e:
            print(e)

    def update_birthdate(self, contador, date):
        sql = f"UPDATE public.characters SET birthdate = '{date}' WHERE id = {contador}"
        try:
            self.cursor.execute(sql)
            self.conection.commit()

        except Exception as e:
            print(e)


bd = Database()
Characters = characters_archive()
powers = powers_archive()
powers_character = powers_character_archive()

#Metodos de insercion de datos a las tablas
# insert_json_powers(poderes)
# insert_json_characters()
# insert_json_powers_character(powers_character)
# bd.add_column_birthdate
# bd.update_birthdate()


# update_dates_random(bd)

# Queries

print(bd.consultas_sql("""select name, birthdate 
from characters"""))

print(bd.consultas_sql("""select count(id) 
from characters 
Group by cit_id"""))

print(bd.consultas_sql("""select ch.name, ct.name, pw.name, pc.level 
from city ct 
INNER JOIN characters ch on ct.id = ch.cit_id
INNER JOIN powers_character pc on  ch.id = pc.cha_id
INNER JOIN powers pw on pc.pow_id = pw.id"""))

print(bd.consultas_sql("""select name,cit_id,description
from characters 
where name LIKE '%u%' """))

print(bd.consultas_sql("""select ch.name, pw.name
from characters ch
INNER JOIN powers_character pc on ch.id = pc.cha_id
INNER JOIN powers pw on pc.pow_id = pw.id
where pw.name LIKE 'Fly' and pw.name LIKE 'SuperForce' and pw.name LIKE 'Telekinesis';
"""))

print(bd.consultas_sql("""select ch.name, pw.name
from characters ch
INNER JOIN powers_character pc on ch.id = pc.cha_id
INNER JOIN powers pw on pc.pow_id = pw.id
where pw.name LIKE 'Fly' or pw.name LIKE 'SuperForce' or pw.name LIKE 'Telekinesis';
"""))

print(bd.consultas_sql("""select id,name,birthdate 
from characters 
WHERE birthdate BETWEEN '2014-02-01' AND '2014-03-01'
"""))

print(bd.consultas_sql("""select id,name,birthdate 
from characters 
where birthdate < '2011-1-1'
"""))

print(bd.consultas_sql("""select ch.name,ch.birthdate, pw.name 
from characters ch
INNER JOIN powers_character pc on ch.id = pc.cha_id
INNER JOIN powers pw on pc.pow_id = pw.id
where pw.name NOT LIKE 'Fly';
"""))


