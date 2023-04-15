# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу x
# Пользователь вводит натуральное число n – количество элементов в массиве и число, которое
# необходимо проверить - x. Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к x элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

import random
while True:
    try:
        kol_el = int(input('Введите количество элементов в списке: '))
        numbers = []

        for i in range(1, kol_el):
            random_num = round(random.randint(0, kol_el))
            numbers.append(random_num)

        print(numbers)

        x = int(
            input('Введите число, к которому будем искать ближайший элемент в списке: '))
        min = x

        for j in numbers:
            difference = abs(x - j)
            if difference == min:
                if result > j:
                    result = j
            if difference < min:
                min = difference
                result = j
        if result == x:
            print('Введенное число есть в списке. Оно и является самым близким.')
        else:
            print(
                f'Cамый близкий по величине элемент к заданному числу {x}: {result}')

        break

    except:
        print('Некорректный ввод! Попробуйте еще раз.')
