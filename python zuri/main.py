import random
from secrets import choice

while True:
     choices = ["rock","paper", "scissors"]

     computer = random.choice(choices)
     player = None
     print("computer: ", computer)

     while player not in choices:
         player = input("rock, paper, or scissors?: ").lower()

         print("player: ",player)

     if player == computer:
         print("tie!")

     elif player == "scissors":
      if computer == "rock":
         print("you lose!")
     if computer == "paper":
         print("you win!")    

     elif  player == "paper":
      if computer == "scissors":
         print("you lose!")
     if computer == "rock":
         print("you win!")

     elif  player == "rock":
      if computer == "paper":
         print("you win!")
     if computer == "scissors":
         print("you win!")

     play_again = input("play again? (yes/no): ").lower()

     if play_again != "yes":
        break

print("bye!")

     