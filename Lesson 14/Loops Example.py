#Loops
for i in range(4):
    print(i)

#0
#1
#2
#3

range(4) # returns a list-like object starting at 0 up to but not including 4
a = 0
b = 4
range(a, b) # returns a list-like object starting at a up to but not including b

c = 2

range(a, b, c) # returns a list-like object starting with a up up to b noninclusive stepping c each time

#range can be used in for-loops to keep track of index
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#Index 0 in supplies is: pens
#Index 1 in supplies is: staplers
#Index 2 in supplies is: flame-throwers
#Index 3 in supplies is: binders

#Multiple Assignment
print('This is a cat')
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size) #'fat'
print(color) #'orange'
print(disposition) #'loud'

print('New Cat')
size, color, disposition = 'skinny', 'black', 'quiet'
print(size) #skinny
print(color)  #black
print(disposition) #quiet

#Swap values
a = "AAA"
b = "BBB"
a, b = b, a
print(a) #BBB
print(b) #AAA


#Increment/Decrement operator
spam = 42
print(spam)
spam += 1
print(spam)

