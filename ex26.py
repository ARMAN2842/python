# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число: '))
b = int(input(f'Введите в какую степень возвести число {a}: '))


def sqr(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return (a * sqr(a, b-1))


print(f'Число {a} в степени {b} равно: {sqr(a, b)}')
