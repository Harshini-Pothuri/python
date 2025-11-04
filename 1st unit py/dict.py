'''d=dict()
d[100]="sri"
d[200]="ram"
d[300]="ram"
print(d)

d={100: 'sri', 200: 'ram',300:"shiva"}
print(d[300])
print(d[100])

#update
d={100: 'sri', 200: 'ram',300:"shiva"}
d[400]="sunny"
print(d)
d[100]="rani"
print(d)
d.update({200:"satya"})
print(d)

#delete
d={100: 'sri', 200: 'ram',300:"shiva"}
del d[100]
print(d)

#clear
d={100: 'sri', 200: 'ram',300:"shiva"}
d.clear()
print(d)'''

d={100: 'sri', 200: 'ram',300:"shiva"}
print(d.get(400,"hi"))
print(d.get(300))


d={100: 'sri', 200: 'ram',300:"shiva"}
del d
print(d)
















