
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = ("a", "b", "c", "d")

print(tup1, tup2, tup3)

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(len(thistuple))

print(type(thistuple))

print(thistuple[1])

print(thistuple[-1])

print(thistuple[2:5])

print(thistuple[:5])

if "apple" in thistuple:
    print("Yes, apple is my favorite fruit")
    
    
x = list(thistuple)
x[1]

x.append("passion")
thistuple = tuple(x)

for x in thistuple:
    print(x)
    
for i in range(len(thistuple)):
    print(thistuple[i])
    
j = 0
while j < len(thistuple):
    print(thistuple[j])
    j += 1