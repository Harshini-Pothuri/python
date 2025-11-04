# Instance Methods
'''class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
            print('Hi',self.name)
            print('Your marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
                print('You got first grade')
        elif self.marks>=50:
                print('You got second grade')
        elif self.marks>=35:
                print('You got third grade')
        else:
                print('You failed')
n=int (input('Enter number of students:'))
for i in range(n):
             name=input('Enter Name:')
             marks=int(input('Enter Marks:'))
             s=student(name,marks)
             s.display()
             s.grade()
             print()



# Class Method
class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noofobjects(cls):
        print('No .of Objects created are:',cls.count)
t1=Test()
t2=Test()
Test.noofobjects()
t3=Test()
t4=Test()
t5=Test()
Test.noofobjects()'''

# Static Method
class Aditya:
    @staticmethod
    def add(x,y):
        print('Addition is:',(x+y))
    @staticmethod
    def sub(x,y):
        print('Subtraction is:',(x-y))
    @staticmethod
    def avg(x,y):
        print('Addition is:',(x+y)/2)
Aditya.add(200,100)
Aditya.sub(200,100)
Aditya.avg(200,100)
        















             
            
