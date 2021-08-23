import random
import time

time.sleep(1)

def start():
    ask = str(input("Hello world, you are in game named rock paper scissors in python! Do you want to play? (yes/no): "))

    if ask == "yes" or ask == "Yes":
        print("Ok, good luck!")
        play()
    else: 
        print("Good bye")
        quit()


def play():
    rps = str(input("rock, paper, scissors, you want: "))

    list = ("rock", "paper", "scissors")

    random_rps = str(random.choice(list))

    print("Bot chose " + random_rps)

    if random_rps == "rock" and rps == "scissors":
        time.sleep(1)
        print("Bot wins, congrats to bot.")
    elif random_rps == "scissors" and rps == "paper":
        time.sleep(1)
        print("Bot wins, congrats to bot.")
    elif random_rps == "paper" and rps == "rock":
        time.sleep(1)
        print("Bot wins, congrats to bot.")

    elif random_rps == "scissors" and rps == "rock":
        time.sleep(1)
        print("Human wins, congrats to human.")
    elif random_rps == "paper" and rps == "scissors":
        time.sleep(1)
        print("Human wins, congrats to human.")
    elif random_rps == "rock" and rps == "paper":
        time.sleep(1)
        print("Human wins, congrats to human.")


    elif random_rps == "rock" and rps == "rock":
        time.sleep(1)
        print("It's a tie")
    elif random_rps == "paper" and rps == "paper":
        time.sleep(1)
        print("It's a tie")
    elif random_rps == "scissors" and rps == "scissors":
        time.sleep(1)
        print("It's a tie")
    again()


def again():
    ask_again = input("Do you want to play again? (yes/no)?: ")
    if ask_again == "yes" or ask_again == "Yes":
        print("Ok, we are going")
        time.sleep(1)
        play()
    else:
        quit()

start()