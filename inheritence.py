# Inheritence
'''class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def Bark(self):
        print("Bark")
d=Dog()
d.sound()
d.Bark()

# Multiple Inheritence
class A:
    def methodA(self):
        print("Method A")
class B:
    def methodB(self):
        print("Method B")
class C(A,B):
    def methodC(self):
        print("Method C")
c=C()
c.methodA()
c.methodB()
c.methodC()

# Multilevel Inheritence
class A:
    def methodA(self):
        print(" A")
class B(A):
    def methodB(self):
        print(" B")
class C(B):
    def methodC(self):
        print(" C")
c=C()
c.methodA()
c.methodB()
c.methodC()'''


# Hierarchical Inheritence
class A:
    def methodA(self):
        print("Method A")
class B(A):
    def methodB(self):
        print("Method B")
class C(A):
    def methodC(self):
        print("Method C")
c1=B()
c2=C()
c1.methodA()
c1.methodB()
c2.methodC()
c2.methodA()


# Hybrid Inheritence
class A:
    def methodA(self):
        print("A")
class B(A):
    def methodB(self):
        print("B")
class C:
    def methodC(self):
        print("C")
class D(B,C):
    pass
d=D()
d.methodA()
d.methodB()
d.methodC()

