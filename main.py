import pandas as pd
from datetime import datetime


# Функция ввода данных студентов
def input_students():
    students = []
    num_students = int(input("Введите количество студентов: "))

    for i in range(num_students):
        print(f"\nВведите данные для студента {i + 1}:")
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        birth_date = input("Дата рождения (ГГГГ-ММ-ДД): ")

        num_subjects = int(input("Количество предметов в зачетке (от 3 до 5): "))
        record_book = []

        for j in range(num_subjects):
            print(f"Введите данные для предмета {j + 1}:")
            subject_name = input("Предмет: ")
            exam_date = input("Дата экзамена (ГГГГ-ММ-ДД): ")
            teacher_name = input("ФИО преподавателя: ")

            record_book.append({
                "Предмет": subject_name,
                "Дата экзамена": exam_date,
                "Преподаватель": teacher_name
            })

        students.append({
            "Фамилия и Имя": f"{last_name} {first_name}",
            "Дата рождения": birth_date,
            "Зачетка": record_book
        })

    return students


def display_students_table(students):
    # Преобразование данных
    data = {
        "Фамилия и Имя": [student["Фамилия и Имя"] for student in students],
        "Дата рождения": [student["Дата рождения"] for student in students]
    }
    df = pd.DataFrame(data)

    # Cортировка по дате рождения
    df["Дата рождения"] = pd.to_datetime(df["Дата рождения"])
    df = df.sort_values(by="Дата рождения")

    # Вывод таблицы
    print("\nТаблица студентов, отсортированная по дате рождения:")
    print(df.to_string(index=False))


def main():
    students = input_students()
    display_students_table(students)


if __name__ == "__main__":
    main()