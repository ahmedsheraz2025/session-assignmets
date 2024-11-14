
import random
guess = random.randint(1,99)

while True:
    user_input: int= int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
    print(guess)
    if user_input < guess:
        print("Your guess is too low")
    elif user_input > guess:
        print("Your guess is too high")
    else:
        print("Well done")
        break