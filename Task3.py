#  Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fib(n):
    count=0
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)
N = int(input('Введите номер числа Фибоначчи: '))
numbers = []
for i in range(1,N+1):
    numbers.append(fib(i))
print(numbers[-1])