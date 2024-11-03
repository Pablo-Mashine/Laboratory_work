# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, separator=','): # Функция поиска общих участников
    group1 = set(str1.split(separator)) # Преобразуем строки в множества, разбивая их по заданному разделителю
    group2 = set(str2.split(separator))
    common = group1.intersection(group2) # Находим общих участников
    return sorted(common)  # Возвращаем отсортированный список общих участников
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
