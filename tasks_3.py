# 1.task
# Найти сумму чисел от 1 до n. Напишите рекурсивную функцию, которая принимает число n и возвращает сумму чисел от 1 до n.
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

print(sum_to_n(5))  # 15

# 2.task
# Напишите рекурсивную функцию, которая принимает целое число и возвращает сумму его цифр.
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123))  # 6

# 3.task
# Напишите рекурсивную функцию, которая определяет, является ли данное число степенью двойки.
def is_power_of_two(n):
    if n == 1:
        return True
    if n == 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

print(is_power_of_two(8))  # True

# 4.task
# Напишите рекурсивную функцию, которая принимает два числа: основание и степень. Функция должна возвращать результат возведения основания в степень.
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))  # 8

# 5.task
# Напишите рекурсивную функцию, которая возвращает n-ое число Фибоначчи.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # 13
