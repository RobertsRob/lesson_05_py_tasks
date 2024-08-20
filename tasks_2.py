# 1.taks
# Напишите функцию, которая принимает целое число n и выводит на экран все числа от 1 до n (включительно).
def print_numbers(n):
    for i in range(1, n+1):
        print(i)

print_numbers(5)

# 2.taks
# Напишите функцию, которая принимает целое число n и выводит на экран таблицу умножения на это число от 1 до 10.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

multiplication_table(3)

# 3.taks
# Создайте функцию, которая принимает два числа a и b, и выводит все числа между ними (включительно).
def print_range(a, b):
    for i in range(a, b+1):
        print(i)

print_range(5, 10)

# 4.taks
# Напишите функцию, которая принимает целое число n и возвращает сумму всех чисел от 1 до n.
def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_numbers(5))

# 5.taks
# Создайте функцию, которая принимает строку и возвращает количество гласных в этой строке.
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello"))

# 6.taks
# Создайте функцию, которая принимает строку и возвращает ее перевернутой.
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("Python"))

# 7.taks
# Создайте функцию, которая принимает строку и возвращает количество слов в этой строке.
def count_words(s):
    count = 1
    for char in s:
        if char == " ":
            count += 1
    return count

print(count_words("Hello world from Python"))

# 8.taks
# Создайте функцию, которая принимает два числа a и b и возвращает сумму всех четных чисел между ними.
def sum_even(a, b):
    total = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            total += i
    return total

print(sum_even(1, 10))

# 9.taks
# Создайте функцию, которая принимает целое число n и выводит на экран все числа Фибоначчи до n.
def fibonacci(n):
    a = 0
    b = 1
    print(a)
    print(b)
    while a < n:
        a = b
        b = a + b
        print(a)

fibonacci(50)

# 10.taks
# Создайте функцию, которая принимает целое число n и выводит на экран все простые числа от 2 до n.
def print_primes(n):
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

print_primes(20)








