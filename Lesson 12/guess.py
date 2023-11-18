import random
# First Complete Program

print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,20)
print (' Well, ' + name + ', I am thinking of a number tween 1 & 20')
       

#ask for guesses
for guessessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your number is too low')
    elif guess > secretNumber:
        print ('Your number is too high')
    else:
        break # Correct Guess kicks out of loop
if guess == secretNumber:
    print(' Great Job!!!')
else:
    print('Nope. The number I was thinking of was )' +  str(secretNumber))
