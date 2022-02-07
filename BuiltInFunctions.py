myList=[1,2,3,4,3,5,3,2,4,3]

print(len(myList)) # len and print is built in function

for i in range(10): # range is built in function
    print(pow(i+1,2), end=' ') # pow is built in function
myList.sort() # len is built in function
print()
def powerList(i): # This is a function
    return pow(i,2)

for i in myList:
    print(powerList(i))

