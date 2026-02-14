num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

num3 = int(input("Enter the third number: "))

num4 = int(input("Enter the fourth number: "))

# Sort the numbers using if-else statements

if num1 > num2:

num1, num2 = num2, num1

if num2 > num3:
  num2, num3 = num3, num2

if num3 > num4:

num3, num4 = num4, num3

if num1 > num2:

num1, num2 = num2, num1

if num2 > num3:

num2, num3 = num3, num2

if num1 > num2:

num1, num2 = num2, num1

# Display the sorted numbers

print("Numbers in sorted order:")

print(num1, num2, num3, num4)
