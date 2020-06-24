"""
Факториал числа n равен произведению всех чисел от 1 до n, то есть:
n! = 1 * 2 * 3 * ... * n

Написать функцию, которая возвращает количество идущих подряд нулей на конце n!.

def get_zeros(n):
....

print(get_zeros(5))
OUT: >> 1

print(get_zeros(12))
OUT: >> 2

Вопросы:
- Какая сложность у вашего алгоритма?
"""


# 1. Получение факториала через библиотеку math, работает быстрее, чем во втором случае
def factorial1(n):
    import math
    result = math.factorial(n)
    return result


# 2. Получение факториала через цикл for, работает медленнее, чем первый вариант
def factorial2(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 3. Подсчет Количества подряд идущий нулей на конце факториала
def get_zeros(factorial):
    if str(factorial).endswith('0'):
        string = str(factorial)
        count = 0
        print(f'Факториал из {n}! равен {factorial}')
        index = -1
        while string[index] == '0':
            count += 1
            index -= 1
        print(f'Количество подряд идущий нулей на конце {factorial} равно: {count}')
    else:
        print('Факториал не содержит нулей на конце числа')
    return


def main():
    n = 5
    # factorial = factorial1(n)   # Можно выбрать любой способ подсчета факториала
    factorial = factorial2(n)
    get_zeros(factorial)


if __name__ == '__main__':
    main()
