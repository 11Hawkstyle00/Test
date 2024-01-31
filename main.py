# Открытие нового CSV-файла для записи
file = open('student_new.csv', 'w')

# Определение данных для класса и их оценки
DB = [
    ('11 М', 3.5),
    ('11 А', 2.5),
    ('10 И', 3.5)
]


# Рассчёт средней оценки по классу
total_grades = 0
id = 1
num_students = len(DB)
for klass, mark in DB:
    total_grades += mark
    id += 1

average_grade = round(total_grades / num_students, 3)

# Нахождение оценки Владимира Хайдарова
vladimir_grade = None
id = 1
for klass, mark in DB:
    id += 1
    if klass == 'Хадаров Владимир':
        vladimir_grade = mark
        break

# Вывод оценки Владимира Хайдарова
print(f"Ты получил: {vladimir_grade}, за проект - {id}")

# Запись данных в CSV-файл
file.write('Класс, Средняя оценка\n')
for klass, mark in DB:
    if mark == '':
        file.write(f'{klass}, {average_grade}\n')
    else:
        file.write(f'{klass}, {mark}\n')

# Закрытие файла
file.close()
