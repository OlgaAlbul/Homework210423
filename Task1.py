# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N 
# ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial (n):
    if n==1:
        return 1
    return n*factorial(n-1)


def triangular_number (n):
    if n==0:
        return 0
    return n+triangular_number(n-1)
N = int(input('Введите число: '))
print(factorial(N))
print(triangular_number(N))


