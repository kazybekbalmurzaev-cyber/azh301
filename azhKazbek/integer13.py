# Integer13: Given a three-digit number, remove the first digit and append it to the end. Output the resulting number.

num = int(input("Enter a three-digit number: "))

# Extract digits
first = num // 100
last_two = num % 100

# Form new number
result = last_two * 10 + first

print(result)