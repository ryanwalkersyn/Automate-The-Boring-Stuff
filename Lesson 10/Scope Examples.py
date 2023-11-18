# Scopes

spam = 42 # global variable

def eggs():
    spam = 69 # nice local variable


'''
# Local variables cannot be used in the General scope
def spam():
    eggs = 99

spam() # after return from function call all local variables are destroyed0
print(eggs) # throws error
'''

# Local Variables in one local scope can't be accessed in another
def spam():
    eggs = 99
    bacon() # the return destroys any local variables created
    print(eggs) # prints current local scope value of eggs

def bacon():
    ham = 101
    eggs = 0

spam()

# Global variables can be used in Local scopes
def spam():
    print(eggs)

eggs = 42 # defines local variable
spam() # doesn't have a local variable eggs so it reads the global variable eggs

# Changing Global variables in Local scopes
def spam():
    global eggs
    eggs = 'Hello'
    print(eggs) # prints "Hello"

eggs = 42
spam()
print(eggs) # prints "Hello"
