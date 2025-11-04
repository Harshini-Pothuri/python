class student:
    '''This is student class with required data'''
print(student.__doc__)
help(student)

class student:
    '''This is student class with required data'''
    def __init__(self):
        self.name="Satya"
        self.age=20
        self.marks=80
    def talk(self):
        print("Hello i am:",self.name)
        print("My age is:",self.age)
        print("My marks are:",self.marks)
s=student()
s.talk()

class student:
    '''Class Demo'''
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def talk(self):
        print("Hello i am:",self.name)
        print("My age is:",self.age)
        print("My marks are:",self.marks)
n=input("Enter name:")
a=int(input("Enter age:"))
m=int(input("Enter marks"))
s=student(n,a,m)
s.talk()

#CONSTRUCTOR:
class test:
    def __init__(self):
        print("constructor execution...")
    def m1(self):
        print("method execution..")
t1=test()
t2=test()
t1.m1()
t2.m1()

class student:
    '''This is student class with required data'''
    def __init__(self,x,y,z):
        self.name=x
        self.rno=y
        self.marks=z
    def display(self):
        print("Student name:{}\nrollno:{}\nmarks:{}".format(self.name,self.rno,self.marks))

s1=student("satya",101,80)
s1.display()
s2=student("sri",102,90)
s2.display()


class student:
    '''This is student class with required data'''
    def __init__(self,name,roll_no):
        #1.instance variable created inside constructor using self
        self.name=name
        self.roll_no=roll_no
        self.age=18
        print("Inside constructor:")
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
        print("Age",self.age)
        
    def update_marks(self,marks):
        #2. Instance variable created inside insrance method using self
        self.marks=marks
        print("\nInside instance method:")
        print(f"{self.name}'s Marks updated to:",self.marks)

    def remove_age(self):
        del self.age
        print("Age instance variable is:")
        print(self.__dict__)

#creating object of the student
s1=student("Anil",101)
s1.update_marks(100)
#3.Accessing and modifying instance variables from outside the cass using object reference
print("\nOutside of class:")
print("Name(before):",s1.name)

#Modifying instance variable
s1.name="Anil Kumar"
print("Name(after):",s1.name)

#calling instance method to add/update marks
s1.update_marks(85)

#Accessing newly added instance variable(marks) from outside
print("Marks(outside):",s1.marks)
s1.remove_age()

#within class del self.variablename  outside the class del objectreference.variable name

'''class student:
    def __init__(self,name,rollno):
        #instance variables created inside constructor using self
        self.name=name
        self.rollno=rollno
        self.age=12
        print("inside constructor")
        print("Name:",self.name)
        print("Rollno:",self.rollno)
        print("Age:",self.age)
        print(self.__dict__)
    def update_marks(self,marks):
        #2.instance variable created/modified inside instance method using self
        self.marks=marks
        print("\ninside instance method:")
        print(f"{self.name}'s Marks updated to:",self.marks)
    def remove_age(self):
        #deleting instance variable inside the class
        del self.age
        print("age instance variable is deleted:")
        print(self.__dict__)
#creating object of student
s1=student("Anil",101)
s1.update_marks(100)
#3.Accessing and modifying instance variables from outside the cass using object referencej
print("\nOutside of class:")
print("Name(before):",s1.name)

#Modifying instance variable
s1.name="Anil Kumar"
print("Name(after):",s1.name)

#calling instance method to add/update marks
s1.update_marks(85)

#Accessing newly added instance variable(marks) from outside
print("Marks(outside):",s1.marks)
s1.remove_age()
#print(s1.age)
#delete instance variable outside the class
del s1.marks
print("\nAfter deleting 'marks' from outside the class:")
print(s1.__dict__)
s2=student("kalpana",102)
s2.update_marks(20)
print(s2.__dict__)'''

class Test:
    x=1
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)





















