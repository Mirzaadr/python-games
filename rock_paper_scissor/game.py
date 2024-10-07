# from random import choice
import random

plays = ["Rock", "Paper", "Scissors"] # define all possible choices

def get_verb(winner, loser):
  verbs = {
      "Rock": {"Scissors": "crushes",},
      "Paper": {"Rock": "covers",},
      "Scissors": {"Paper": "cuts",},
  }
  return verbs[winner][loser] 

def main():
  running = True

  while running:
    computer = random.choice(plays)

    player = input("Rock, Paper, Scissors? (Type 'exit' to quit) ").capitalize()  # get player's choice
    if player.lower() == 'exit':  # check if the player wants to exit
      print("Thanks for playing!")
      break

    if player not in plays:
      print("Not a valid play, PLease choose {}".format(plays))
      continue

    if player == computer:
      print("Tie!")
    elif (player == "Rock" and computer == "Scissors") \
      or (player == "Paper" and computer == "Rock") \
      or (player == "Scissors" and computer == "Paper"):
      print(f"You win! {player} {get_verb(player, computer)} {computer}.")
    else:
      print(f"You lose! {computer} {get_verb(computer, player)} {player}.") 
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
      print("Thanks for playing!")
      break

if __name__ == "__main__":
  main()