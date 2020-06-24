"""
Дан массив целых чисел array и целое число k. Нужно вывести все уникальные пары чисел из массива, сумма которых равна k.
Примечание: под уникальностью понимается следующее: если ответу удовлетворяет несколько пар вида (a, b) и (b, a),
то достаточно вывести только одну пару (a, b).


def search_pairs(array, k):
....

print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))

OUT: >> [(1, 4), (2, 3)]

Вопросы:
- Какая сложность у вашего алгоритма?  - O(n^2)
- Можно ли его оптимизировать?

"""


def search_pairs(array, k):  # полный перебор всех пар
    pairs = []
    for item in range(len(array)):
        for offset_item in range(item + 1, len(array)):
            if array[item] + array[offset_item] == k:
                # если сумма парных элементов = k проверяем, есть ли в уже данная пара в двух вариантах в списке
                # если нет, пишем в список
                if (array[item], array[offset_item]) not in pairs and (array[offset_item], array[item]) not in pairs:
                    pairs.append((array[item], array[offset_item]))
    return pairs


def main():
    array = [1, 2, 6, 5, 3, 4, 7, 8, 3, 2]
    k = 5
    search_pairs(array, k)
    print(search_pairs(array, k))


if __name__ == '__main__':
    main()
