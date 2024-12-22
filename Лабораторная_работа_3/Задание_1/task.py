class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name       # Делаем атрибуты защищенными
        self._author = author       # Делаем атрибуты защищенными

    @property
    def name(self) -> str:      # Геттер для названия книги
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:        # Геттер для автора книги
        """Возвращает автора книги."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)      # Вызываем конструктор базового класса
        self.pages = pages

    @property
    def pages(self) -> int:     # Геттер для страниц в книге
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:    # Сеттер для страниц в книге
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть целым числом.")     # Исключение
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным.")   # Исключение
        self._pages = new_pages

    def __repr__(self):     # Перегрузка метода __repr__, метод __str__ наследуется
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ Дочерний класс аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # Вызываем конструктор базового класса
        self.duration = duration

    @property
    def duration(self) -> float:    # Геттер для продолжительности аудиокниги
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):   # Сеттер продолжительности аудиокниги
        """Устанавливает продолжительность аудиокниги."""
        if not isinstance(new_duration, (float, int)):
            raise TypeError("Продолжительность должна быть числом с плавающей запятой.")    # Исключение
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительной.")    # Исключение
        self._duration = float(new_duration)

    def __repr__(self):     # Перегрузка метода __repr__, метод __str__ наследуется
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
