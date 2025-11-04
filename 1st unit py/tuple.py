'''t=10,20,30
print(t)
print(type(t))

t=(10)
print(t)
print(type(t))

t=(10,)
print(t)
print(type(t))

t=()
print(t)
print(type(t))

t=(10,20,30,40,50)
print(t[0])
print(t[-1])

t=(10,20,30,40,50)
print(t[::2])
print(t[0:3:1])

t=(10,20,30,40,50)
print(len(t))

t=(10,20,30,40,10)
print(t.count(10))
if 30 in t:
    print(t.index(30))
else:
    print("Element not found")

t=(40,10,20,30)
t1=sorted(t)
t2=sorted(t,reverse=True)
print(t)
print(t1)
print(t2)'''

t=(10,20,30,40,50)
print(max(t))
print(min(t))







