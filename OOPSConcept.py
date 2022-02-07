class Person():
    def __init__(self,name,age,branch):
        print("I am calling constructor")
        self.name=name
        self.age=age
        self.branch=branch
        print(f"My name is {name}")
    print("I am in class Person")
    def insidePerson(self,name):
        print("I am inside insidePerson")
        print(f"And Your name is {name}")
class Teacher(Person):
    # def __init__(self,name,age,branch):
    #     print("Hello i am constructor of teacher class")
    print("I am teaching you here")
    def HOD(self):
        print("I am HOD here")

p = Person("Vinay Kumar",20,"EC")
p1 = Person("***ABCD***",30,"CS")
p.name="Kumar Vinay"
p.insidePerson(p.name)
print("--------------")
# p.HOD() Error shows as child parent
t=Teacher("vin",15,"IOT")
t.insidePerson("K")