'''n=[10,20,30,40]
print(n)
n[1]=777
print(n)
print(n[1])
# This gives error print(n[10])

n=[1,2,3,4,5,6,7,8,9]
print(n[2:7:2])
print(n[-1:-10:-1])
print(n[2::2])
print(n[2:8])

#Traversing
n=[1,2,3,4,5,6,7,8,9]
i=0
print("\nUsing while loop")
while i<len(n):
    print(n[i])
    i=i+1
print("\nUsing for loop")
for n1 in n:
    print(n1)

#count
n=[1,2,2,2,2,3,3,4,4,4]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.index(3))
print(n.index(4))'''

n=[1,2,3,4]
flag=0
print(n)
k=int(input("enter value to search: "))
for i in n:
      if(i==k):
          flag=1
          break
      else:
          flag=0
if(flag==1):
    print("Element found")
else:
    print("Element not found")


n=[1,2,3,4]
i=0
print(n)
k=int(input("enter value to search: "))

while i<len(n):
    if(n[i]==k):
        print("Element found")
        break
    else:
         print("Element not found")
         break
    i=i+1


'''list=[1,2,3,4,5,6,7,8]
list.append('a')
list.append('b')
list.append('c')
print(list)

list=[]
for i in range(10):
    list.append(i)
    i=i+1
print(list)

#insert
n=[1,2,3,4,5]
n.insert(1,8888)
print(n)

n=[1,2,3,4,5]
n.insert(-1,8888)
print(n)

list1=["chicken","Mutton","Fish"]
list2=["RC","KF"]
list1.extend(list2)
print(list1)

order=["Chicken","Mutton","Fish"]
order.extend("Mushroom")
print(order)

n=[10,20,30,10]    #n=[10,20,30,10] remove(40)==>error there is not 40
n.remove(10)
print(n)

n=[10,20,30,40,50]
n.pop()
print(n)

n=[10,20,30,40,50]
n.reverse()
print(n)

n=[100,20,10,60,50]
n.sort()
print(n)

n=["dog","apple","ant"]
n.sort(reverse=False)  #True gives ascending order reverse in reverse
print(n)

#Using mathematical opertors for list operators
#Both are must be list datatype
a=[10,20,30]
b=[40,50]
c=a+b
print(c)

n=[10,20,30]
c=n+[25]
print(c)

#Repetition Operator(*)

n=[10,20,30]
print(n*3)

#Comparing operators
a=["dog","apple","cat"]
b=["dog","apple","cat"]
c=["Dog","Apple","Cat"]
print(a==b)
print(a==c)
print(a!=b)


#Membership Operator
n=[10,20,30,40,50]
print(10 in n)
print(90 in n)
print(10 not in n)
n.clear()
print(n)

#-nested list#

n=[[10,20,30],[40,50,60],[70,80,90]]

print(n)

print("Elements by Row wise:")

for r in n:

    print(r)

print("Elements by matrix style:")

for i in range(len(n)):

   for j in range(len(n[i])):

       print(n[i][j],end=" ")

   print()'''


















