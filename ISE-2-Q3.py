n = int(input("Enter a three digit number: "))

first = n // 100
last = n % 10

sum = first + last

print("Sum of first and last digit:", sum)