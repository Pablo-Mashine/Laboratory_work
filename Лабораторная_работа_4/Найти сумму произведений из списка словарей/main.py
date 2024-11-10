# TODO решите задачу
# Импортируем модуль json
import json

"""Функция расчета суммы произведений"""
def task(data: list[dict]) -> float:
    return sum([num['score']*num['weight'] for num in data]) # находим сумму произведений согласно условию


"""Читаем данные из файла в формате JSON"""
with open('input.json', 'r') as file: # Открываем файл для чтения
    data = json.load(file) # Выполняем десериализацию данных из файла в объект Python с помощью метода load

print(round(task(data), 3)) # Выводим результат
