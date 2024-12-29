# TODO: описать базовый класс
class Machine:
    """ Базовый класс для транспорта. """

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param make: Производитель транспорта.
        :param model: Модель.
        :param year: Год выпуска.
        """
        self._make = make  # Производитель
        self._model = model  # Модель
        self._year = year  # Год выпуска

    @property
    def make(self) -> str:  # Геттер для производителя ТС.
        """ Возвращает производителя. """
        return self._make

    @property
    def model(self) -> str:  # Геттер для модели ТС.
        """ Возвращает модель. """
        return self._model

    @property
    def year(self) -> int:  # Геттер для года выпуска ТС.
        """ Возвращает год выпуска. """
        return self._year

    def engine(self) -> str:
        """ Запускает двигатель ТС. """
        return f"{self.make} {self.model} engine started."

    def __str__(self) -> str:
        return f"Производитель {self.make}. Модель {self.model}. Год выпуска {self.year}."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"


# TODO: описать дочерний класс
class Car(Machine):
    """ Класс легкового автомобиля, наследующийся от Machine """

    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Инициализация легкового автомобиля.

        :param make: Производитель легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param doors: Количество дверей в легковом автомобиле.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self._doors = doors  # Количество дверей

    @property
    def doors(self) -> int:  # Геттер для количества дверей автомобиля
        """ Возвращает количество дверей автомобиля. """
        return self._doors

    def engine(self) -> str:
        """ Запускает двигатель легкового автомобиля, выводит дополнительное сообщение о готовности к поездке. """
        return f"{super().engine()} Ready to go!"

    def __str__(self) -> str:
        return f"{super().__str__()} с {self.doors} дверьми."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r}, doors={self.doors!r})"
