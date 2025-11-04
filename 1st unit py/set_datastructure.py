s=set()
print(s)
print(type(s))

s={}
print(s)
print(type(s))

#update
s={10,20,30}
l=[40,50,60,70]
s.update(l,range(5))
print(s)

#copy
s={10,20,30}
s1=s.copy()
print(s1)

#pop
s={10,20,30,40,50,60}
print(s.pop())
print(s)

#remove
s={40,10,30,20}
s.remove(30)   #gives error if we remove 50 bcoz it is present in the set
print(s)

#discard
s={40,10,30,20}  #doesn't gives error if we discard 50 
s.discard(10)
print(s)
s.discard(50)
print(s)

#clear
s={40,10,30,20}
print(s)
s.clear()
print(s)

#Mathematical operations on set
# 1.union x.union(y) or x|y
x={40,10,30,20}
y={10,30,60,70}
print(x.union(y))

# 2. intersection x.intersection(y) or x&y
x={40,10,30,20}
y={10,30,60,70}
print(x.intersection(y))

# 3.Difference x.difference(y) or x-y
x={40,10,30,20}
y={10,30,60,70}
print(x.difference(y))
print(y-x)

#Symmetric_difference x.symmetric_difference(y) or x^y
x={40,10,30,20}
y={10,30,60,70}
print(x.symmetric_difference(y))











