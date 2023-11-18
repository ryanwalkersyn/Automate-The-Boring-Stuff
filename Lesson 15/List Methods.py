###---Methods---###

### List Methods

#Index
spam = ['hello', 'hi', 'howdy', 'heyas','hi']
print(spam.index('hello')) # 0
#index finds the first index which the argument appears in
print(spam.index('hi')) # 1


#Insert/Append
spam = ['cat', 'dog', 'bat']
      
spam.append('moose')
print(spam) #['cat', 'dog', 'bat', 'moose']

spam.insert(1, 'chicken')
print(spam) #['cat', 'chicken', 'dog', 'bat', 'moose']


#Remove - for removing the first instance of the specified argument
spam.remove('bat')
print(spam) #['cat', 'chicken', 'dog', 'moose']
#only the first instance would be removed


#Del - for removing an item at a specific index
del spam[0]
print(spam) #['chicken', 'dog', 'moose']

#Sort
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam) #[-7, 1, 2, 3.14, 5]

eggs = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
eggs.sort()
print(eggs) #['ants', 'badgers', 'cats', 'dogs', 'elephants']

#can only be used on all strings or all numbers (ints/floats)
#sort order for string is ASCII-betical
#to sort in true alphabetical, pass "key=str.lower" into the sort method
