# TODO Найдите количество книг, которое можно разместить на дискете
VOLUME = 1.44 * 1024 * 1024
NUMBER_OF_PAGES = 100
NUMBER_OF_LINES = 50
NUMBER_OF_CHARACTERS = 25
ONE_BYTE = 4
one_book = NUMBER_OF_PAGES * NUMBER_OF_LINES * NUMBER_OF_CHARACTERS * ONE_BYTE
number_of_books = VOLUME // one_book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
