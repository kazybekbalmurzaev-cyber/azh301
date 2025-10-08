# Дано трехзначное число. Найти сумму и произведение его цифр.

number = int(input("Введите трехзначное число: "))

# Проверим, что число действительно трехзначное
if 100 <= number <= 999:
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10

    digit_sum = hundreds + tens + units
    digit_product = hundreds * tens * units

    print("Сумма цифр:", digit_sum)
    print("Произведение цифр:", digit_product)
else:
    print("Ошибка: число не является трехзначным.")