n=int(input("Enter number:"))

temp=n

rev=0

while(n>0):

digit=n%10 # Get the last digit

rev=rev*10+digit # Build the reversed number

n=n//10 # Remove the last digit from the number

if(temp==rev):

print("The number is a palindrome!")

else:

print("The number isn't a palindrome!")
