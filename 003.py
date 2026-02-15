# uses of break statement in for and while loop

# using for loop
for i in range(1,6):
  if (i==3):
    break
  print(i)


# using while loop

numbers=[50,30,20,40,10]
index=0
key=int(input("enter the number you want to search"))
while(1):
  if (numbers[index]==key):
    break
  index=index+1
print(f"the element {key} is found at the position {index}")
