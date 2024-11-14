import random

print("----Welcome to the High-Low Game!----")
def game_engine():
    
    round = 0
    score = 0
    while round < 5 :
        round += 1
        
        print(F" - Round {round} -")
        computer_number = random.randint(1,100)
        my_number = random.randint(1,100)
        print(f"The computer's number is {computer_number}")
        print(f"Your number is {my_number}")
        
        
        print(f"Your score is Now {score}")
        my_choice = input("Do you think your number is higher or lower than the computer's? ")
    
        higher_and_correct = my_choice.lower() == "higher" and my_number > computer_number
        lower_and_correct = my_choice.lower() == "lower" and my_number < computer_number
        
        if higher_and_correct or lower_and_correct:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect Your score: {score}")
            
    if score == 5:
        print("Wow! You played perfectly!")
    elif score == 2:
        print("Good job, you played really well!")
    elif score == 1:
        print("Better luck next time!")
    
game_engine()

