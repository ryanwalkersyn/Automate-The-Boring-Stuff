#Lists

spam = ['Cat', 'Dog', 'Rat', 'Elephant']

# lists start at 0
print(spam[0]) #'cat'

print(spam[1]) #'dog'

# lists can be index negatively
print(spam[-1]) #'elephant'

#slices contain 2 indexes, start and end index, noninclusive
print(spam[1:3]) # ['dog', 'rat']

# lists can contain lists
eggs = [spam, ['Rabbit', 'Horse', 'Fish']]

#elements of internal lists can be accessed with additional index reference
print(eggs[0][1]) # 'dog'


#elements in lists can be changed
spam[0] = 'Frog'
print(spam)

#slices can also be changed
spam[1:3] = ['Monkey', 'Turtle']
print(spam) #['Frog', 'Monkey', 'Turtle', 'Elephant']


#slices can be started or ended without reference
print(spam[:2]) #['Frog', 'Monkey']

print(spam[1:]) #['Monkey', 'Turtle', 'Elephant']

#Len returns list length
print(len(spam)) # 4

#elements can be removed
del spam[2]
print(spam) #['Frog', 'Monkey', 'Elephant']

#in and not in
print('Elephant' in spam) # True

print('Monkey' not in spam) # False
