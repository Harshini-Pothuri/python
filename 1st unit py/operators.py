#Arthhmetic Operators
#For multiple comments use '''
#if b=0 a%b,a/b,a//b gives an error
a=10
b=2
'''print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
print("a%b=",a%b)
print("a//b=",a//b)
print("a**b=",a**b)
c=5.0
print("c/b=",c/b)
print("c//b=",c//b)
print("durga"+"10")
print('\n')
#Relational Operators
a,b=10,20

print(a,'>',b,'=',a>b)
print(a,'>=',b,'=',a>=b)
print(a,'<',b,'=',a<b)
print(a,'<=',b,'=',a<=b)
print(a,'==',b,'=',a==b)
print(a,'!=',b,'=',a!=b)
print("\n")
a='satya'
b='satya'
print('a>b=',a>b)
print('a>=b=',a>=b)
print('a<b=',a<b)
print('a<=b=',a<=b)
print('a==b=',a==b)
print('a!=b=',a!=b)

print("\n")
print(True>True)
print(True>=False)
print(10>True)
print(False>True)
print("\n")
#Write a program for printing roll no and name
rollno=int(input("Enter roll no:"))
name=input("Enter your name:")
print('Roll no is ',rollno)
print('Name is \n',name)'''

#Bitwise Operators
'''print(4&5)
print(4|5)
print(4^5)
print(True&True)
print(10>>2)
print(10>>3)

print(True&True)
print(True|False)
print(True^False)
print(~True)
print(True<<2)
print(True>>2)'''

#Terninary operators
a,b=10,20
x=30 if a<b else 40
print(x)
print("\n")

#Special Operators
#1.Identity operator(is and is not)
a,b=10,20
print(a is b)
print(a is  not b)
print("\n")
#2.Membership(string,list,tuple,dict)(in and not in)
x="Hello There"
print('h' in x)
print('Hello' in x)
print("\n")

list=("Hi","Hello","Bye")
print("hi" in list)
print("There" in list)
print("There" not in list)
print("\n")



