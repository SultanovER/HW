import sqlite3

db = sqlite3.connect('students.db')
c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students(
id INTEGER,
name TEXT,
surname TEXT,
yearborn INTEGER,
hobby TEXT,
points INTEGER
)''')

c.execute('''INSERT INTO students VALUES (1, 'Анатолий', 'Ивановский', 1987 ,'Полёт', 11)''')
c.execute('''INSERT INTO students VALUES (2, 'Семён', 'Антонов', 1997 ,'Есть', 9)''')
c.execute('''INSERT INTO students VALUES (3, 'Владимир', 'Гольдштейн', 1980 ,'Книги', 20)''')
c.execute('''INSERT INTO students VALUES (4, 'Иван', 'Шестьянов', 2005 ,'Полёт', 2)''')
c.execute('''INSERT INTO students VALUES (5, 'Роман', 'Комиссаров', 2005 ,'Столярное дело', 1)''')
c.execute('''INSERT INTO students VALUES (6, 'Олег', 'Майковский', 1960 ,'Математика', 10)''')
c.execute('''INSERT INTO students VALUES (7, 'Тимур', 'Найзинян', 2000 ,'Стрельба', 5)''')
c.execute('''INSERT INTO students VALUES (8, 'Алёна', 'Андреева', 2008 ,'Кухня', 7)''')
c.execute('''INSERT INTO students VALUES (9, 'Амалия', 'Тарковская', 1994 ,'Фильмы', 9)''')
c.execute('''INSERT INTO students VALUES (10, 'Исмаил', 'Бекджанов', 2015 ,'Вырез бумаги', 3)''')

c.execute('''SELECT * from students WERE LENGHT(surname) > 10''')
c.execute('''UPDATE students SET name == 'Genius' WHERE points > 10''')
c.execute('''DELETE FROM students WHERE id % 2 == 0''')
db.commit()
db.close()
