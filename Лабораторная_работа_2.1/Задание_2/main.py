import sys
sys.path.insert(0, '../Задание 1')
from task import Mug
from task import Airplane
from task import Dog

if __name__ == "__main__":
    # Тестирование класса Mug
    try:
        mug = Mug("красный", 250, True)
        print(mug.fill(200))  # Кружка наполнена на 200 мл.
        print(mug.get_info())  # Кружка цвета красный, вместимость: 250 мл, нержавеющая: True.

        # Проверка на исключение
        print(mug.fill(300))  # Исключение
    except ValueError as e:
        print(e)

    # Тестирование класса Airplane
    try:
        airplane = Airplane("Airbus A320", 180, 2000)
        print(airplane.fly(1000))  # Самолет Airbus A320 полетел на 1000 км.
        print(airplane.get_info())  # Самолет модели Airbus A320, вместимость: 180, год выпуска: 2000.

        # Проверка на исключение
        print(airplane.fly(-500))  # Исключение
    except ValueError as e:
        print(e)

    # Тестирование класса Dog
    try:
        dog = Dog("Шарик", "Дворняга", 5)
        print(dog.bark(2))  # Шарик лает 2 раз(а).
        print(dog.get_info())  # Собака по имени Шарик, порода: Дворняга, возраст: 5 года.

        # Проверка на исключение
        print(dog.bark(0))  # Исключение
    except ValueError as e:
        print(e)