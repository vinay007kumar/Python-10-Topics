import math
squareList=[]
normalList=[]
square=10
#                                   while loop
while(square):
    squareList.append(square ** 2)
    square -=1
print("squareList is : ",squareList)
squareList.sort()
print("Sorted List of squareList is : ",squareList)

def sqRoot(n):
    return i ** 0.5
#                                   for loop
for i in squareList:
    n= sqRoot(i)
    normalList.append(n)
print("Square Root List is : ",normalList)

