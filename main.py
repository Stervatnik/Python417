# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
#
#
# def keep(todo1):
#     is_complete = todo1['completed']
#     has_max_count = str(todo1['userId']) in users
#     return is_complete and has_max_count
#
# with open("filtred_data.json","w") as f:
#     filtred_todos = list(filter(keep, todos))
#     json.dump(filtred_todos, f, indent=2)
#
# with open("filtred_data.json","r") as f:
#     print(json.load(f))
#
#
# import csv
#
# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {','.join(row)}')
#         else:
#             print(f'\t{row[0]} - {row[1]}. Родился в {row[2]} году')
#         count += 1
#
#
#     print(f'Всего в файле {count} строки.')
#
#
# import csv
#
# with open("data.csv") as f:
#
#     file_names = ['Имя', "Профессия", "Год рождения"]
#
#
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {','.join(row)}')
#
#         print(f'\t{row['Имя']} - {row["Профессия"]}. Родился в {row['Год рождения']} году.')
#
#         count += 1
#
#
# import csv
#
# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', 'Класс', 'Возраст'])
#     writer.writerow(['Женя',9, 15])
#     writer.writerow(['Саша',5, 12])
#     writer.writerow(['Маша',11, 17])
#
#
#
# import csv
#
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     for row in data:
#         writer.writerows(row)
#
#
#
# import csv
#
#
# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerows(data)
#
#
#
# import csv
#
#
# with open('student.csv', 'w') as f:
#     names = ['Имя', 'Возраст']
#     writer = csv.DictReader(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({'Имя': 'Саша', 'Возраст': 6})
#     writer.writerow({'Имя': 'Маша', 'Возраст': 15})
#     writer.writerow({'Имя': 'Вова', 'Возраст': 14})
#
#
#
# import csv
#
#
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
#
#
# https://jsonplaceholder.typicode.com/todos Домашнее задание из json в csv
#
#
#
#
#
# ПАРСИНГ ДАННЫХ С САЙТОВ
#
# from bs4 import BeautifulSoup
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
#
#
#
#
# row = soup.find('div', class_='name').text
# row = soup.find_all('div', class_='name')
# row = soup.find_all('div', class_='row')[2].find('div', class_='name').text
# row = soup.find_all('div', class_='row')[2].find('div', {'class':'name'}).text
# row = soup.find_all('div', {'data-set': 'salary'})
# row = soup.find_all('div', string = 'Alena')
# row = soup.find('div', string = 'Alena').parent
# row = soup.find('div', string = 'Alena').parent.parent
# row = soup.find('div', string = 'Alena').find_parent(class_='row')
# row = soup.find('div', id='whois3').text
# row = soup.find('div', id='whois3').find_next_sibling()
# row = soup.find('div', id='whois3').find_previous_sibling()
#
# print(row)
#
# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois')
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
#
# copywriter = []
# row = soup.find_all('div', class_='row')
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
#
#
# print(copywriter)
#
#
# from bs4 import BeautifulSoup
# import re
#
#
#
# def get_salary(s):
#     pattern = r'\d+'
#     res = re.findall(pattern, s)[0]
#     print(res)
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
#
#
# def get_copywriter(tag):
#     whois = tag.find('div', class_='whois')
#     if 'Copywriter' in whois:
#         return tag
#     return None
#
# row = soup.find_all('div', {'data-set': 'salary'})
# for i in row:
#     get_salary(i.text)
#
#
#
#
#
# import requests
# from bs4 import BeautifulSoup
#
#
#
#
# # r = requests.get('https://ru.wordpress.org/')
# # print(r.text)
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find('h1', class_='wp-block-heading').text
#     return p1
#
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()
#
#
#
#
# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refined(s):
#     return re.sub(r'\D+', '', s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';',lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('section', class_='plugin-section')[2]
#     plugins = p1.find_all('li')
#     for plugin in plugins:
#         name = plugin.find('h3', class_='entry-title').text
#         # url = plugin.find('h3', class_='entry-title').find('a').get('href')
#         url = plugin.find('h3', class_='entry-title').find('a')['href']
#         rating = plugin.find('span', class_='rating-count').text
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#     # return plugins
#
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     (get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()
#
#
#
# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
#
# # r = requests.get('https://ru.wordpress.org/')
# # print(r.text)
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def refind_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8-sig') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['snippet'],data['active'], data['tested']))
#
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     p1 = soup.find_all('li', class_='wp-block-post')
#     for el in p1:
#         name = el.find('h3', class_='entry-title').text
#         url = el.find('h3', class_='entry-title').find('a')['href']
#         snippet = el.find('div', class_='entry-excerpt').text.strip()
#         active = el.find('span', class_='active-installs').text.strip()
#         test = el.find('span', class_='tested-with').text.strip()
#         cy = refind_cy(test)
#         data = {'name': name, 'url': url, 'snippet': snippet, 'active': active, 'tested': cy}
#         write_csv(data)
#
#
#
# def main():
#     for i in range(3, 23):
#         url = f'https://ru.wordpress.org/plugins/browse/blocks/page/{i}/'
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
#
#
#
#
# from parser import Parser
#
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
#     pars.run()
#
#
#
#
#
# if __name__ == '__main__':
#     main()
#
#
#
#
# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT "+79991234567",
#     age INTEGER CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )""")
#
#
# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     ALTER TABLE person
#     RENAME TO person_table;
#     """)
#
# Добавление столбца
# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     ALTER TABLE person_table
#     ADD COLUMN address TEXT;
#     """)
#
# Переименование столбца
# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     ALTER TABLE person_table
#     RENAME COLUMN address TO home_address;
#     """)
#
# Удаление столбца
# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     ALTER TABLE person_table
#     DROP COLUMN home_address;
#     """)
#
# Удаление таблицы
# import sqlite3
#
# with sqlite3.connect('users.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     DROP TABLE person_table;
#     """)
#
#
#
# import sqlite3
#
# with sqlite3.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         LIMIT 2, 5;
#     """)
#
#     for res in cur:
#         print(res)
#
#
# import sqlite3
#
# with sqlite3.connect('db_3.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#         SELECT *
#         FROM T1
#         LIMIT 2, 5;
#     """)
#
#     # res2 = cur.fetchall()
#     # print(res2)
#
#     # res3 = cur.fetchone()
#     # print(res3)
#
#     res4 = cur.fetchmany(2)
#     print(res4)
#
#
# def sum1(args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
# list = ['a', 'b', 'c', 'd']
# print(sum1(list))
#
#
# import sqlite3
#
# with sqlite3.connect('person.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS companies(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL)
#
#     """)
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     company_id INTEGER,
#     FOREIGN KEY(company_id) REFERENCES companies(id) ON DELETE SET NULL)
#     """)
#
#
# import sqlite3
#
# with sqlite3.connect('book.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS books(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     count_pages INTEGER NOT NULL CHECK (count_pages > 0),
#     price REAL CHECK (price > 0))
#
#     """)
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS author(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER CHECK (age > 16)
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS author_books(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     books_id INTEGER NOT NULL,
#     author_id INTEGER NOT NULL,
#     FOREIGN KEY(books_id) REFERENCES books(id)
#     FOREIGN KEY(author_id) REFERENCES author(id)
#     )""")
#
#
#
#
# Домашнее задание
# import sqlite3
#
# with sqlite3.connect("education.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS student(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT NOT NULL,
#     name TEXT NOT NULL,
#     patronymic  TEXT NOT NULL,
#     age INTEGER NOT NULL CHECK(age >= 17 AND age <= 50),
#     [group] TEXT NOT NULL,
#     FOREIGN KEY ([group]) REFERENCES groups (id) ON DELETE RESTRICT
#     )""")
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS groups(
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        group_name TEXT NOT NULL)
#        """)
#
#     cur.execute("""
#      CREATE TABLE IF NOT EXISTS lessons(
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      lesson_title TEXT NOT NULL
#      )""")
#
#     cur.execute("""
#      CREATE TABLE IF NOT EXISTS association(
#      group_id INTEGER,
#      lesson_id INTEGER,
#      PRIMARY KEY (group_id, lesson_id)
#      FOREIGN KEY (group_id) REFERENCES groups(id)
#      FOREIGN KEY (lesson_id) REFERENCES lessons(id)
#      )""")
#
#
#
#
# import sqlite3
#
# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
#
# with sqlite3.connect('automobile.db') as conn:
#     cur = conn.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     # cur.execute("INSERT INTO cars VALUES (1, 'Renault', 22000)")
#     # cur.execute("INSERT INTO cars VALUES (1, 'Volvo', 29000)")
#     # cur.execute("INSERT INTO cars VALUES (1, 'Mersedes', 57000)")
#     # cur.execute("INSERT INTO cars VALUES (1, 'Bentley', 35000)")
#     # cur.execute("INSERT INTO cars VALUES (1, 'Audi', 52000)")
#
#
#     # for car in cars_list:
#     #     cur.execute("INSERT INTO cars VALUES (NULL, ?, ?)", car)
#
#
#     # cur.executemany("INSERT INTO cars VALUES (NULL, ?, ?)", cars_list)
#
#
#     # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})
#
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)
#
#
# import sqlite3
#
# con = None
#
# try:
#     conn = sqlite3.connect('automobile.db')
#     cur = conn.cursor()
#     cur.executescript("""
#     BEGIN;
#     INSERT INTO cars VALUES (NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     conn.commit()
#
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print('Ошибка выполнения запроса')
# finally:
#     if conn:
#         conn.close()
#
#
#
# import sqlite3
#
# with sqlite3.connect('automobile.db') as con:
#     con.row_factory = sqlite3.Row
#
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)" )
#     # last_id = cur.lastrowid
#     # buy_id = 2
#     # cur.execute("INSERT INTO cost VALUES('Илья',?, ?)", (last_id, buy_id))
#
#     cur.execute("SELECT model, price FROM cars")
#     for res in cur:
#         print(res['model'], res['price'])
#
#     # print(cur.fetchall())
#     # print(cur.fetchone())
#     # print(cur.fetchmany(5))
#     # print(cur.fetchall())
#
#
#
# import sqlite3
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         return False
#
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#     #     return False
#     # return True
#
#
# with sqlite3.connect('automobile.db') as con:
#     con.row_factory = sqlite3.Row
#
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#
#     );
#     """)
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES ('Илья', ?, 1000)", (binary, ))
#
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#     write_ava('out.png', img)
#
#
# import sqlite3
#
# # with sqlite3.connect('automobile.db') as con:
# #     cur = con.cursor()
# #
# #     with open("sql_dump.sql", 'w') as f:
# #
# #         for sql in con.iterdump():
# #             f.write(sql)
#
#
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)
#
# ______________________________________________________________________________________________
#
#
# import os
#
# from models.database import DATABASE_NAME
# import create_database as db_creator
#
# if __name__ == '__main__':
#     db_is_creator = os.path.exists(DATABASE_NAME)
#     if not db_is_creator:
#         db_creator.create_database()
#
#
# ______________________________________________________________________________________________
#
#
#
#
# from jinja2 import Template
#
#
# name = "Игорь"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет. Меня зовут {{ n.upper() }}.")
# msg = tm.render(n=name, a=age)
#
# print(msg)
#
#
#
#
# per = {'name': "Игорь", 'age': 28}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p['name'] }}.")
# msg = tm.render(p=per)
#
# print(msg)
#
#
#
#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select>
#     {% for c in cities %}
#         {% if c.id > 3 %}
#             <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#         {% elif c.city == 'Москва' %}
#             <option>{{ c['city'] }}</option>
#         {% else %}
#             {{ c['city'] }}
#         {% endif %}
#     {% endfor %}
# </select>>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)
# НАДО ДОПИСАТЬ+++++++++++++++++++++++++++++++++++++
# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# link = """<ul>
#     {% for i in menu %}%}
#         {% if i.link == 'Главная' %}
#         <li><a href= '{{ i['href'] }}' class='active'</li> ЗДЕСь
#         <li><a href='{{ i['href'] }}'> {{ i ['link'] }} </a></li>
#         {% endif %}
#     {% endfor %}
# </ul>"""
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)
# +++++++++++++++++++++++++++++++++++++++++++++++++
#
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44200},
#     {'model': 'Volkswagen', 'price': 31300},
# ]
#
#
# # tpl = "{{ cs | sum(attribute='price') }}"
# # tpl = "{{ cs | min(attribute='price').model }}"
# # tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
#
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)
#
# from jinja2 import Template
#
# persons = [
#     {"name": 'Алексей', "year": 18, "weight": 78.5},
#     {"name": 'Никита', "year": 28, "weight": 82.3},
#     {"name": 'Виталий', "year": 32, "weight": 94.1},
# ]
#
# tpl = """
# {% for u in users %}
# {% filter upper %}{{ u.name }}{% endfilter %}
#
# {% endfor %}
#
# """
#
#
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)
#
#
#
#
# from jinja2 import Template
#
#
# html = """
# {% macro fun_input(name, value="", type='text', size=20) %}
#     <input type = "{{ type }}" name = "{{ name }}" value = "{{ value }}" size = "{{ size }}" >
#
# {% endmacro %}
#
# <p>{{ fun_input('username', '', 'text', 40) }}</p>
# <p>{{ fun_input('email', 'Email', 'email') }}</p>
# <p>{{ fun_input('password', 'Пароль', 'password') }}</p>
# """
#
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)
#
#
#
#
#
# from jinja2 import Template
#
# persons = [
#     {"name": 'Алексей', "year": 18, "weight": 78.5},
#     {"name": 'Никита', "year": 28, "weight": 82.3},
#     {"name": 'Виталий', "year": 32, "weight": 94.1},
# ]
#
#
# html = """
# {% macro list_users(list_of_user) %}
#     <ul>
#         {% for u in list_of_user %}
#             <li> {{ u.name }} {{ caller(u) }} </li>
#         {% endfor %}
#     </ul>
# {% endmacro %}
#
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li> age: {{ user.year }} </li>
#         <li> weight: {{ user.weight }} </li>
#     </ul>
# {% endcall %}
#
#
#
# """
#
# # {{ list_users(users) }}
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)
#
#
#
# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {"name": 'Алексей', "year": 18, "weight": 78.5},
#     {"name": 'Никита', "year": 28, "weight": 82.3},
#     {"name": 'Виталий', "year": 32, "weight": 94.1},
# ]
#
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('home.html')
# msg = tm.render(users=persons, title='About Jinja')
#
# print(msg)
#
# import sqlite3
#
# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sqlite3.connect('automobile.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS auto(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     ''')
#
#     cur.execute('INSERT INTO auto VALUES(1, "Renault", 22000)')
#     cur.execute('INSERT INTO auto VALUES(2, "Volvo", 29000)')
#     cur.execute('INSERT INTO auto VALUES(3, "Mercedes", 57000)')
#     cur.execute('INSERT INTO auto VALUES(4, "Bentley", 35000)')
#     cur.execute('INSERT INTO auto VALUES(5, "Audi", 52000)')
#     for car in cars_list:
#         cur.execute("INSERT INTO auto VALUES(NULL, ?, ?)", car)
#
#     cur.executemany('INSERT INTO auto VALUES(NULL, ?, ?)', cars_list)
#
#     cur.execute('UPDATE auto SET price = :Price WHERE model LIKE "B%"', {"Price": 0})
#
#     cur.executescript('''
#     DELETE FROM auto WHERE model LIKE "B%";
#     UPDATE auto SET price = price + 100;
#     ''')
#
#
# import sqlite3
#
# con = None
#
# try:
#     con = sqlite3.connect('automobile.db')
#     cur = con.cursor()
#     cur.executescript("""
#     BEGIN;
#     INSERT INTO auto VALUES(NULL, 'Renault', 25000);
#     UPDATE auto SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()
#
# import sqlite3
#
# with sqlite3.connect('automobile.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS auto(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT,
#         tr_in INTEGER,
#         buy INTEGER
#     );
#     ''')
#     cur.execute("INSERT INTO auto VALUES(NULL, 'Москвич', 1000)")
#     last_id = cur.lastrowid
#     buy_id = 2
#     cur.execute("INSERT INTO cost VALUES('Дмитрий', ?, ?)", (last_id, buy_id))
#
#     cur.execute("SELECT model, price FROM auto")
#     # for res in cur:
#     #     print(res[0], res[1])
#
#     for res in cur:
#         print(res['model'], res['price'])
#
#     print(cur.fetchall())
#
#     print(cur.fetchone())
#     print(cur.fetchmany(5))
#     print(cur.fetchall())
#
#
# import sqlite3
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#     #     return False
#     # return True
#
# with sqlite3.connect('automobile.db') as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     ''')
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES ('Дмитрий', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users ")
#     img = cur.fetchone()['ava']
#     write_ava("out.png", img)
#
#
# import sqlite3
#
# with sqlite3.connect('automobile.db') as con:
#     cur = con.cursor()
#
#     with open("sql_dump2.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)
#
#
# import sqlite3
#
# with sqlite3.connect('avto.db') as conn:
#     cur = conn.cursor()
#
#     with open("sql_dump2.sql", "r") as sql_file:
#         sql = sql_file.read()
#         cur.executescript(sql)
#
#
#
#
# --------------------------------------------------------------
# import os
#
#
# from models.database import DATABASE_NAME
# import create_database as db_creator
#
# if __name__ == "__main__":
#     db_is_creator = os.path.exists(DATABASE_NAME)
#     if not db_is_creator:
#         db_is_creator.create_database()
# --------------------------------------------------------------
#
# from jinja2 import Template
#
# name = "Дмитрий"
# age = 32
#
# tm = Template("Мне {{ age*2 }} года. Меня зовут {{ name.upper() }}.")
# msg = tm.render(name=name, age=age)
#
# print(msg)
#
#
# from jinja2 import Template
#
# per = {"name": "Дмитрий",
#        "age": 32}
#
# tm = Template("Мне {{ per.age }} года. Меня зовут {{ per.name }}.")
# msg = tm.render(per=per)
#
# print(msg)
#
#
# from jinja2 import Template
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# per =  Person("Дмитрий",32)
#
# tm = Template("Мне {{ per.age }} года. Меня зовут {{ per.name }}.")
# msg = tm.render(per=per)
#
# print(msg)
#
#
# from jinja2 import Template
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#
# per =  Person("Дмитрий",32)
#
# tm = Template("Мне {{ per.get_age() }} года. Меня зовут {{ per.name }}.")
# msg = tm.render(per=per)
#
# print(msg)
#
#
#
# from jinja2 import Template
#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select>
#     {% for c in cities %}
#         <option value="{{ c.id }}">{{ c.city }}</option>
#     {% endfor %}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)
#
#
#
# from jinja2 import Template
#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Сочи'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select>
#     {% for c in cities %}
#         {% if c.id > 3 %}
#             <option value="{{ c.id }}">{{ c.city }}</option>
#
#         {% elif c.city == "Москва" %}
#             <option>{{ c.city }}</option>
#         {% else %}
#             {{ c.city }}
#         {% endif %}
#     {% endfor %}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)
#
#
# from jinja2 import Template
#
# menu = [
#     {"href": "/index", "link": "Главная"},
#     {"href": "/news", "link": "Новости"},
#     {"href": "/about", "link": "О компании"},
#     {"href": "/shop", "link": "Магазин"},
#     {"href": "/contacts", "link": "Контакты"},
# ]
#
# link = """ <ul>
#     {% for i in menu %}
#         {% if i.link == 'Главная' %}
#             <li><a href='{{ i.href }}' class='active'>{{ i.link }}</a></li>
#         {% else %}
#             <li><a href='{{ i.href }}'>{{ i.link }}</a></li>
#         {% endif %}
#     {% endfor %}
# </ul>"""
#
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)
#
# from jinja2 import Template
#
# cars = [
#     {"model": "Audi", "price": 23000},
#     {"model": "Mazda", "price": 32000},
#     {"model": "Mercedes", "price": 45000},
#     {"model": "Subaru", "price": 53000},
# ]
#
# tpl = "{{ cs | sum(attribute='price') }}"
# tpl = "{{ cs | max(attribute='price') }}"
# tpl = "{{ (cs | max(attribute='price')).model }}"
# tpl = "{{ (cs | min(attribute='price')).model }}"
# tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
#
#
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)
#
# from jinja2 import Template
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.},
#     {"name": "Виталий", "year": 32, "weight": 94.1},
# ]
#
# tpl = '''
# {% for u in users %}
#     {% filter upper %}{{ u.name }}{% endfilter %}
# {% endfor %}
#
# '''
#
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)
#
# from jinja2 import Template
#
#
# html = """
# {% macro fun_input(name, value='', type='text', size=20) %}
#     <input type = "{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}" >
# {% endmacro %}
#
# <p>{{ fun_input('username', '', 'text', 40) }}</p>
# <p>{{ fun_input('email', 'Email', 'email') }}</p>
# <p>{{ fun_input('password', 'Пароль', 'password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)
#
#
#
#
# from jinja2 import Template
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.},
#     {"name": "Виталий", "year": 32, "weight": 94.1},
# ]
#
# html = """
# {% macro list_users(list_of_user) %}
#     <ul>
#         {% for u in list_of_user %}
#             <li>{{ u.name }} {{ caller(u) }}</li>
#         {% endfor %}
#     </ul>
#
# {% endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>age: {{ user.year }}</li>>
#         <li>age: {{ user.weight }}</li>>
#     </ul>
# {% endcall %}
#
#
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)
#
#
# from jinja2 import Environment, FileSystemLoader
#
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.},
#     {"name": "Виталий", "year": 32, "weight": 94.1},
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('home2.html')
# msg = tm.render(users=persons, title='About Jinja')
#
# print(msg)
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# {% for z in zap %}
#   <p><input type="{{z.type}}" name="{{ z.name }}" placeholder="{{z.placeholder }}"></p>
# {% endfor %}
#
# <p><input type="type" name="name" placeholder="placeholder"></p>
#
#
# from jinja2 import Environment, FileSystemLoader
#
#
# inputs = [
#     {"type": "text", "name": "firstname", "placeholder": "имя"},
#     {"type": "text", "name": "lastname", "placeholder": "фамилия"},
#     {"type": "text", "name": "address", "placeholder": "адрес"},
#     {"type": "tel", "name": "phone", "placeholder": "телефон"},
#     {"type": "email", "name": "email", "placeholder": "почта"},
#
# ]
#
#
#
# file_loader = FileSystemLoader('Dom33')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('base.html')
# msg = tm.render(zap=inputs)
# print(msg)
#
#
#
# from jinja2 import Environment, FileSystemLoader
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render()
# print(msg)
#
#
#
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# import os
# from sqlalchemy import create_engine, Column, Integer, String, Float
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from faker import Faker
#
# # 1. Определение модели таблицы
# Base = declarative_base()
#
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     email = Column(String)
#     age = Column(Integer)
#     salary = Column(Float)
#
#     def __repr__(self):
#        return f"<User(first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', age={self.age}, salary={self.salary})>"
#
#
# # 2. Создание подключения к базе данных
# # Используем SQLite в памяти для простоты примера,
# # но можно заменить на URL реальной базы данных
# DATABASE_URL = "sqlite:///:memory:"  # Или "sqlite:///./test.db" чтобы создать файл
# engine = create_engine(DATABASE_URL, echo=True) # echo=True для логирования SQL запросов
# Base.metadata.create_all(engine)  # Создаем таблицу в базе данных
#
# # 3.  Настройка сессии
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# session = SessionLocal()  # Создаем экземпляр сессии
#
# # 4. Генерация и добавление фейковых данных
# fake = Faker()
# NUMBER_OF_RECORDS = 10
#
# for _ in range(NUMBER_OF_RECORDS):
#     fake_user = User(
#         first_name=fake.first_name(),
#         last_name=fake.last_name(),
#         email=fake.email(),
#         age=fake.random_int(min=18, max=65),
#         salary=fake.pyfloat(left_digits=5, right_digits=2, positive=True)
#     )
#     session.add(fake_user)
#
# # 5.  Подтверждение изменений и закрытие  сессии
# session.commit() #  Записываем изменения в базу данных
#
# # 6.  Пример запроса и вывода данных
# users = session.query(User).all()
# for user in users:
#     print(user)
#
# session.close()
#
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
#
# import os
#
#
# from models.database import DATABASE_NAME
# import create_database as db_creator
#
# if __name__ == "__main__":
#     db_is_creator = os.path.exists(DATABASE_NAME)
#     if not db_is_creator:
#         db_is_creator.create_database()
#
#
#
# print("Hello")
# print("hello")




print("Проверка репозитория")