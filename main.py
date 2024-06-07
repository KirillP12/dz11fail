"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

from input import input_data as inp
from print import print_data as pr
from search import search_data as se
import shutil


import os

def main_menu():
    print('Добро пожаловать в телефонный справочник!')
    while(True):
        answer = input('1) Сделать запись\n 2) Найти\n 3) Вывести всё\ n4) Выйти\n Введите вариант: ')
        if answer == '1':
            inp()
        elif answer == '2':
            se()
        elif answer == '3':
            pr()
        elif answer == "4":
            shutil.move('old_directory/file.txt', 'new_directory/new_file_1.txt')
        elif answer == '5':
            print('\nВсего доброго!')
            break
        else:
            print('\nТакого варианта нет.\n')

os.system('cls||clear')
main_menu()