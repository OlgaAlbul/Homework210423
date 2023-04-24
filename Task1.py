# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N 
# ЧЕРЕЗ РЕКУРСИЮ и без циклов

def factorial (n):
    if n==1:
        return 1
    return n*factorial(n-1)
N = int(input('Введите число: '))
print(factorial(N))
