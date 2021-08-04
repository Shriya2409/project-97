import random

intro="Number guessing game - Guess a number between 1 and 9"
print(intro)
guess=int(input("enter your guess: "))
print(guess)

number=random.randint(1,9)
if(guess>number):
    print("Your guess was too high. The number is")
    print(number)
elif(guess<number):
    print("Your guess was too low. The number is")
    print(number)
else:
    print("Congratulations YOU WON!!")
