# python script to rotate right about a given position in that list and display them.

# Create a List
myList =[1,4,5,-10]

print("List before rotation = ",myList)

# The value of n for rotation position

n=int(input("Enter rotation position:"))

# Rotating the List

if n>len(myList):

n = int(n%len(myList))

myList = (myList[-n:] + myList[:-n])

# Display the Update List after rotation

print("Updated List after rotation = ",myList)
