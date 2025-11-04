#Operator Overloading
'''class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return (self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
p1=point(1,2)
p2=point(2,4)
print(p1+p2)


class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return (self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
p1=point(6,2)
p2=point(2,4)
p3=point(0,0)
p3=p1+p2
print(p3)


class student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def __eq__(self,other):
        return self.rno==other.rno,self.name==other.name
s1=student("Anil",101)
s2=student("Ravi",101)
print(s1==s2)

#Method Overloading
class demo:
    def greet(self,name=None):
        if name:
            print(f"Hello,{name}")
        else:
            print("Hello")
obj=demo()
obj.greet()
obj.greet("Anil")

#Variable length
class calculator:
    def add(self,*args):
        return sum(args)
c=calculator()
print(c.add(2))
print(c.add(2,3))
print(c.add(1,2,3))

#constructor overloading(not directly supported by python)
class Demo:
    def __init__(self,name=None,rollno=None):
        if name and rollno:
            print(f"Name:{name},Rollno:{rollno}")
        elif name:
            print(f"Name:{name}")
        elif rollno:
            print(f"Rollno:{rollno}")
        else:
            print("No details")
s1=Demo()
s2=Demo("Kalpana",448)
s3=Demo("Hema")
s4=Demo(353)'''

#Exception handling try-except
try:
    n=int(input("enter a number:"))
    print(f"You entered:{n}")
except ValueError:
    print("That's not a valid number! Please enter an integer")
    print("Program continues after the try-except block:")
try:
    #code that may raise an exception
    x=10/0
except ZeroDivisionError:
    print("Cannot divide by Zero")


try:
    num=int(input("Enter a number"))
    print(10/num)
except ZeroDivisionError:
    print("cannot divide bt zero!")
except ValueError:
    print("Invalid Input!")
else:
    print("No Exception Occured")
finally:
    print("Excecution Complete")
















