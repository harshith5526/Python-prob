# Read an n-digit integer
n = int(input("Enter the number of digits: "))
if n > 0:
number = int(input(f"Enter a {n}-digit integer: "))
# Check if the entered number has n digits
if number >= 10 ** (n - 1) and number < 10 ** n:
# Separate and display each digit using floor and mod operators
for _ in range(n):
digit = number // (10 ** (n - 1))
print(digit, end=' ')
number %= 10 ** (n - 1)
n -= 1
else:
print(f"Please enter a {n}-digit integer.")
else:
print("Please enter a valid number of digits (greater than 0).")
