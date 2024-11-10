# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

"""Функция конвертации из CSV в JSON формат"""
def task(input_filename):
    # TODO считать содержимое csv файла
    # Считываем содержимое csv файла
    with open(input_filename, 'r') as file: # Открываем файл для чтения
        reader = csv.DictReader(file, delimiter = ',') # Читаем данные из файла csv в виде словарей с помощью метода DictReader
        data = [row for row in reader] # Преобразуем reader в список словарей

    # TODO Сериализовать в файл с отступами равными 4
    with open("output.json", 'w') as file: # Создаём файл для записи
        json.dump(data, file, indent=4) # Сериализуем данные и записываем их в файл с разделителем 4


if __name__ == '__main__':

    # Нужно для проверки
    task(INPUT_FILENAME)

    # Выводим содержимое файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
