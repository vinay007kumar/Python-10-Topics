with open("FfirstFile.txt","a") as f: # open in append mode
    f.write("My name is vinay kumar yadav")
    f.write("\n")


with open("FfirstFile.txt", 'r') as f: # open in read mode
    a=f.read()
    print(a)

with open("FfirstFile.txt", 'r+') as f: #open in read and write mode
    a=f.read()
    a += "Some text Added Later"
    f.write(a)
    print(a)