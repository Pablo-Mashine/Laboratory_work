# TODO: Подробно описать три произвольных класса


# TODO: описать класс
class Mug:
    def __init__(self, color: str, capacity: float, is_stainless: bool):
        """
        Создание и подготовка к работе объекта "Кружка"

        :param color: Цвет кружки.
        :param capacity: Объем кружки в миллилитрах.
        :param is_stainless: Является ли кружка нержавеющей.
        :raises ValueError: Если объем меньше или равен нулю.

        Примеры:
        >>> mug = Mug("оранжевый", 500, True)  # инициализация экземпляра класса
        """
        if capacity <= 0:
            raise ValueError("Объем кружки должен быть больше нуля.")

        self.color = color
        self.capacity = capacity
        self.is_stainless = is_stainless

    def fill(self, amount: float) -> str:
        """
        Функция, которая заполняет кружку.

        :param amount: Количество жидкости для наливания в миллилитрах.
        :raises ValueError: Если amount меньше или равно нулю или превышает объем.
        :return: Строка с сообщением о наполнении кружки.

        Примеры:
        >>> mug = Mug("синий", 300, True)
        >>> mug.fill(250)
        'Кружка наполнена на 250 мл.'
        """
        if amount <= 0:
            raise ValueError("Количество жидкости должно быть больше нуля.")
        if amount > self.capacity:
            raise ValueError("Количество жидкости превышает объем кружки.")

        return f'Кружка наполнена на {amount} мл.'

    def get_info(self) -> str:
        """
        Функция, которая выводит информацию о кружке.

        :return: Строка с информацией о кружке.

        Примеры:
        >>> mug = Mug("синий", 300, True)
        >>> mug.get_info()
        'Кружка цвета синий, объем: 300 мл, нержавеющая: True.'
        """
        return f'Кружка цвета {self.color}, объем: {self.capacity} мл, нержавеющая: {self.is_stainless}.'

# TODO: описать ещё класс
class Airplane:
    def __init__(self, model: str, capacity: int, year: int):
        """
        Создание и подготовка к работе объекта "Самолет"

        :param model: Модель самолета.
        :param capacity: Вместимость самолета (количество пассажиров).
        :param year: Год выпуска самолета.
        :raises ValueError: Если год выпуска меньше 1900 или вместимость меньше или равна нулю.

        Примеры:
        >>> airplane = Airplane("Boeing 747", 416, 2005) # инициализация экземпляра класса
        """
        if year < 1900:
            raise ValueError("Год выпуска должен быть не ранее 1900 года.")
        if capacity <= 0:
            raise ValueError("Вместимость самолета должна быть больше нуля.")

        self.model = model
        self.capacity = capacity
        self.year = year

    def fly(self, distance: float) -> str:
        """
        Функция, которая выполняет полет самолета.

        :param distance: Расстояние в километрах.
        :raises ValueError: Если distance меньше или равно нулю.
        :return: Строка с сообщением о полете.

        Примеры:
        >>> airplane = Airplane("Boeing 747", 416, 2005)
        >>> airplane.fly(1500)
        'Самолет Boeing 747 полетел на 1500 км.'
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть больше нуля.")

        return f'Самолет {self.model} полетел на {distance} км.'

    def get_info(self) -> str:
        """
        Функция, которая выводит информацию о самолете.

        :return: Строка с информацией о самолете.

        Примеры:
        >>> airplane = Airplane("Boeing 747", 416, 2005)
        >>> airplane.get_info()
        'Самолет модели Boeing 747, вместимость: 416, год выпуска: 2005.'
        """
        return f'Самолет модели {self.model}, вместимость: {self.capacity}, год выпуска: {self.year}.'
# TODO: и ещё один
class Dog:
    def __init__(self, name: str, breed: str, age: int):
        """
        Создание и подготовка к работе объекта "Собака"

        :param name: Имя собаки.
        :param breed: Порода собаки.
        :param age: Возраст собаки в годах.
        :raises ValueError: Если возраст меньше 0.

        Примеры:
        >>> dog = Dog("Бобик", "Французский Бульдог", 3) # инициализация экземпляра класса
        """
        if age < 0:
            raise ValueError("Возраст собаки не может быть отрицательным.")

        self.name = name
        self.breed = breed
        self.age = age

    def bark(self, times: int = 1) -> str:
        """
        Функция, которая воспроизводит лай собаки.

        :param times: Количество раз, которое собака будет лаять (по умолчанию 1).
        :raises ValueError: Если times меньше или равно нулю.
        :return: Строка с сообщением о лайе собаки.

        Примеры:
        >>> dog = Dog("Булька", "Французский Бульдог", 9)
        >>> dog.bark(3)
        'Булька лает 3 раз(а).'
        """
        if times <= 0:
            raise ValueError("Собака должна гавкнуть хотя-бы один раз.")

        return f'{self.name} лает {times} раз(а).'

    def get_info(self) -> str:
        """
        Функция, которая выводит информацию о собаке.

        :return: Строка с информацией о собаке.

        Примеры:
        >>> dog = Dog("Бобик", "Французский Бульдог", 3)
        >>> dog.get_info()
        'Собака по имени Бобик, порода: Французский Бульдог, возраст: 3 года.'
        """
        return f'Собака по имени {self.name}, порода: {self.breed}, возраст: {self.age} года.'


if __name__ == "__main__":
    import doctest
    doctest.testmod()