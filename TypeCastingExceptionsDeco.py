num= 34
print(type(num))
numstr = str(num) # type casting
str="My name is Vinay"
print(type(numstr))

# This is exception handling
try:
    print(7/0)
except:
    print("An error occured")
else:
    print("No error occured. Executed when no exception is occured")
finally:
    print("Definately Executed")

#Decorators

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()

print("Example of Decorators")
@a_new_decorator
def a():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a()
#outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

#the @a_new_decorator is just a short way of saying:
a = a_new_decorator(a)