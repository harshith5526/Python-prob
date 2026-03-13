n=int(input("Enter the number:"))

#convert the given number into string and then into list

digits = list(str(n))

n1=int(input("Enter first position for interchange:"))

n2=int(input("Enter second position for interchange:"))

#swap the given digits in the list at the given indices

digits[n1], digits[n2] = digits[n2], digits[n1]

#Convert the list back to an integer

result = int(''.join(digits))

print(f"Input: {n}, Interchanged: {result}")
