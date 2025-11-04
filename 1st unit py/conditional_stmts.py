#If
'''name=input("Enter name:")
if name=="satya":
    print("Hello")
print("Bye")
#else-if
name=input("Enter name:")
if name=="satya":
    print("Hello")
else :
    print("Bye")

#Write the program for biggest of three numbers.
x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
z=int(input("Enter z value:"))
if x>y and x>z:
    print("Larsgest number is:",x)
elif y>x and y>z:
    print("Larsgest number is:",y)
else:
    print("Larsgest number is:",z)

#write a program when number enters it has to appear in words

x=int(input("Enter x value:"))
if x==0:
    print("Zero")
elif x==1:
    print("one")
elif x==2:
    print("two")
elif x==3:
    print("three")
elif x==4:
    print("four")
elif x==5:
    print("five")
elif x==6:
    print("six")
elif x==7:
    print("seven")
elif x==8:
    print("eight")
elif x==9:
    print("nine")
else :
    print("It is not a single digit number")

#Iterative statements
n=int(input("Enter n value:"))
for x in range(n):
    if x%2==0:
        print(x)

n=int(input("Enter n value:"))
for n in range(n,0,-1):
    print(n)

s=input("Enter string:")
for ch in s:
    print(ch,end=" ")

for x in range(4):
    for y in range(4):
        print(y,end=" ")
    print(" ")

n=int(input("Enter n value: "))
for i in range(1,n+1):
    print("*"*i)

#While loop
x=1
while x<=10:
     print(x)
     x=x+1

n=int(input("Enter n value:"))
sum , i=0,1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)


#Break
for i in range(10):
    if(i==7):
        print("Break here")
        break
    print(i)

cart=[10,200,600,500]
for item in cart:
    if item>=500:
        print("Break")
        break
    print(item)

n=int(input("Enter no.of subjects:"))
for i in range(n):
    i=int(input("Enter one subject marks"))
    if i<30:
        print("Fail")
    else :
        print(i)

#continue:
num=[10,20,0,5,0,30]
for n in num:
    if n==0:
        print("processing is enough...please continue")
        continue
    print("100/{}={}".format(n,100/n))

#List datatype

list=eval(input("Enter list:"))
print(list)
print(type(list))

#list using function
l=list(range(0,10,2))
print(l)
print(type(l))'''

#list using split
s="Hii there My name is Harshini"
n=s.split()
print(n)
print(type(n))

      




