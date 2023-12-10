#!/usr/bin/env python3Х
# -*- coding: utf-8 -*-
# Использовать словарь, содержащий следующие ключи:
# фамилия и инициалы; номер группы; успеваемость (список из пяти элементов).
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по алфавиту;
# вывод на дисплей фамилий и номеров групп для всех студентов, имеющих хотя бы одну оценку 2;
# если таких студентов нет, вывести соответствующее сообщение.
# Оформить каждую команду в виде отдельной функции.
# Необходимо дополнительно реализовать сохранение и чтение данных из файла формата JSON.
# Необходимо также проследить за тем,
# чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной работы.
# Реализовать интерфейс командной строки (CLI).

import argparse
import json


def input_data():
    students = []
    n = int(input("Введите количество студентов: "))
    for i in range(n):
        student = {"фамилия и инициалы": input("Введите фамилию и инициалы студента: "),
                   "номер группы": input("Введите номер группы студента: "), "успеваемость": []}
        for j in range(5):
            mark = int(input(f"Введите оценку {j + 1}: "))
            student["успеваемость"].append(mark)
        students.append(student)
    students.sort(key=lambda x: x["фамилия и инициалы"])
    return students


def save_data(students, filename):
    with open(filename, "w") as file:
        json.dump(students, file, ensure_ascii=False)


def read_data(filename):
    with open(filename, "r") as file:
        students = json.load(file)
        students.sort(key=lambda x: x["фамилия и инициалы"])
        return students


def print_students_with_mark2(students):
    found = False
    for student in students:
        if 2 in student["успеваемость"]:
            print(f"Студент: {student['фамилия и инициалы']}, группа: {student['номер группы']}")
            found = True
    if not found:
        print("Нет студентов с оценкой 2")


def main():
    parser = argparse.ArgumentParser(description="Process student data")
    parser.add_argument("--filename", help="Имя файла для сохранения/загрузки данных", default="students.json")
    args = parser.parse_args()

    students = input_data()
    save_data(students, args.filename)

    students = read_data(args.filename)
    print_students_with_mark2(students)


if __name__ == "__main__":
    main()
