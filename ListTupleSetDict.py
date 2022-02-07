myList=[] #Empty List Contains any types of values
myDict={} #Empty Dict contains key anf values pairs
myTuple=() #Empty tuple they are immutable
mySet=set() # Empty Set contain different values only
print(type(myList))
print(type(myDict))
print(type(myTuple))
print(type(mySet))
a1=[
    {
        "RollNo": "35",
        "Name": "ddbd"
    },
    {
        "RollNo": "567",
        "Name": "dbdb"
    }
]
print((type(a1)))
myList2=[1,2,3,4,3,5,3,2,4,3]
myList.append(34)
# myList.extend(34) not possible as only extend another list
myList.extend('40')
myList.insert(2,40)
myList.extend(myList2)
print("3 Appres in myList is :",myList.count(3),"times.")
myList.pop()
print("Now 3 Appres in myList is :",myList.count(3),"times.")
print(myList)

mySet2 = set('45')
print(mySet2)
