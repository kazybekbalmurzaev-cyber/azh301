# Дано трехзначное число. Вывести его последнюю цифру (единицы), затем среднюю цифру (десятки).

number = int(input("Введите трехзначное число: "))

last_digit = number % 10
middle_digit = (number // 10) % 10

print(last_digit)
print(middle_digit)