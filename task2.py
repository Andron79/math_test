"""
В этой задаче, помимо алгоритма, нужно указать ответ числом.

Есть файл с именами (https://yadi.sk/i/97rbNP2ucGoAKw). Нужно выполнить следующие действия и посчитать результат:

1) Отсортировать все имена в лексикографическом порядке
2) Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39)
3) Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном списке (индексация начинается с 1).
   Например, если MAY находится на 63 месте в списке, то результат для него будет 63 * 39 = 2457.
4) Просуммировать произведения из третьего пункта по всем именам из файла.

В качестве ответа надо прислать код и число из пункта 4.   - Контрольная сумма: 871853874
"""

import string


def sort_alphabet(file):
    # составляем словарь-алфавит с индексированными буквами и читаем файл
    alphabet = dict([tuple(reversed(character)) for character in enumerate(string.ascii_uppercase, 1)])

    with open(file, 'r') as f:
        text = f.read()

    # 1. Очистка и сортировка списка имен в лексикографическом порядке
    items = (text[1:-1].replace('"', '').split(','))
    items.sort()

    # 2. Подсчет для каждого имени алфавитной суммы
    def func(names: list):
        s = sum([alphabet[name] for name in names])
        return s

    sum_character_list = list(map(func, items))
    print(sum_character_list)

    # 3, 4. Умножаем алфавитную сумму на порядковый номер и выводим искомое число
    count, result = 1, 0
    for item, value in zip(items, sum_character_list):
        print(f'{item} - алфавитная сумма - {value}')
        result = result + value * count
        count += 1

    print('_______________________________')
    print(f'Контрольная сумма: {result}')
    print('_______________________________')


def main():
    sort_alphabet('names.txt')


if __name__ == '__main__':
    main()
