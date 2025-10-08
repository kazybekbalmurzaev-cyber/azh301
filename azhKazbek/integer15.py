# Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков.

number = int(input("Введите трехзначное число: "))

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

# Меняем сотни и десятки местами
new_number = tens * 100 + hundreds * 10 + units

print("Результат:", new_number)