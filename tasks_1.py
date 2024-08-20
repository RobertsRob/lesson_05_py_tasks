# 1.task
# Создайте функцию print_info, которая принимает параметры name, age и city и выводит информацию о человеке в формате "Имя: name, Возраст: age, Город: city". Вызовите функцию, передавая аргументы в произвольном порядке.
def print_info(name, age, city):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

print_info(city="Рига", name="Алексей", age=30)

# 2.task
# Создайте функцию calculate_circle_area, которая принимает радиус и возвращает площадь круга. Вызовите эту функцию с радиусом 7 и выведите результат.
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2

area = calculate_circle_area(7)
print(f"Площадь круга с радиусом 7: {area}")

# 3.task
# Создайте функцию calculate_rectangle_perimeter, которая принимает длину и ширину прямоугольника и возвращает его периметр. Вызовите эту функцию для прямоугольника с длиной 7 и шириной 5, затем выведите результат.
def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

perimeter = calculate_rectangle_perimeter(7, 5)
print(f"Периметр прямоугольника с длиной 7 и шириной 5: {perimeter}")

# 4.task
# Создайте функцию convert_to_celsius, которая принимает температуру в Фаренгейтах и возвращает её в градусах Цельсия. Вызовите эту функцию с температурой 98.6 и выведите результат. (°C = (°F - 32) × 5/9)
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = convert_to_celsius(98.6)
print(f"Температура 98.6°F в градусах Цельсия: {celsius}")

# 5.task
# Создайте функцию increment_counter, которая увеличивает глобальную переменную counter на переданное значение. Вызовите эту функцию несколько раз и выведите значение counter до и после каждого вызова.
counter = 0

def increment_counter(value):
    global counter
    counter += value

print(f"До вызова функции: {counter}")
increment_counter(3)
print(f"После вызова функции: {counter}")
increment_counter(5)
print(f"После второго вызова функции: {counter}")

# 6.task
# Создайте функцию calculate_interest, которая принимает сумму депозита, процентную ставку и количество лет (по умолчанию 1 год) и возвращает сумму через указанное количество лет с простым процентом. Вызовите функцию с разными значениями параметров.
def calculate_interest(principal, rate, years=1):
    return principal * (1 + rate * years / 100)

total_amount_1_year = calculate_interest(1000, 5)
total_amount_5_years = calculate_interest(1000, 5, 5)
print(f"Сумма через 1 год: {total_amount_1_year}")
print(f"Сумма через 5 лет: {total_amount_5_years}")

# 7.task
# Создайте функцию find_max, которая принимает три числа и возвращает наибольшее из них. Вызовите эту функцию и выведите результат.

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

max_number = find_max(3, 7, 5)
print(f"Наибольшее число: {max_number}")

# 8.task
# Создайте функцию calculate_discount, которая принимает сумму покупки и тип клиента (regular или vip). Для regular клиентов скидка 5%, для vip - 10%. Если тип клиента не указан, используйте regular. Функция должна возвращать сумму со скидкой. Вызовите функцию для разных типов клиентов и выведите результаты.
def calculate_discount(total_amount, client_type="regular"):
    if client_type == "regular":
        discount = 0.05
    elif client_type == "vip":
        discount = 0.10
    else:
        pass
    return total_amount * (1 - discount)

total_regular = calculate_discount(1000)
total_vip = calculate_discount(1000, "vip")
print(f"Сумма со скидкой для regular: {total_regular}")
print(f"Сумма со скидкой для vip: {total_vip}")

# 9.task
# Создайте функцию can_travel, которая принимает параметры age (возраст), has_passport (есть ли паспорт) и has_visa (есть ли виза). Функция должна возвращать True, если возраст больше 18, есть паспорт и виза. Вызовите функцию с разными значениями параметров и выведите результаты.
def can_travel(age, has_passport, has_visa):
    if age > 18 and has_passport == "да" and has_visa == "да":
        return True
    else:
        return False

travel_status_1 = can_travel(20, "да", "да")
travel_status_2 = can_travel(17, "да", "нет")
print(f"Статус поездки 1: {travel_status_1}")
print(f"Статус поездки 2: {travel_status_2}")

# 10.task
# Создайте функцию generate_report, которая принимает следующие параметры:
# - student_name (имя студента)
# - test_score (набранные баллы)
# - total_score (максимально возможные баллы)
# - passing_score (процент прохождения)
# Функция должна рассчитать процент набранных баллов и сравнить его с процентом прохождения. Если процент набранных баллов меньше процента прохождения, вернуть строку вида "Не сдал. Процент набранного балла: X%", где X — процент набранных баллов. Если процент набранных баллов равен или больше процента прохождения, вернуть строку вида "Сдал. Процент набранного балла: X%", где X — процент набранных баллов.
def generate_report(student_name, test_score, total_score, passing_score):
    percentage_score = (test_score / total_score) * 100
    if percentage_score < passing_score:
        return f"{student_name} не сдал. Процент набранного балла: {percentage_score}%"
    else:
        return f"{student_name} сдал. Процент набранного балла: {percentage_score}%"

print(generate_report("Иван", 45, 60, 50))  # Иван сдал. Процент набранного балла: 75.00%
print(generate_report("Мария", 30, 60, 50))  # Мария не сдала. Процент набранного балла: 50.00%
