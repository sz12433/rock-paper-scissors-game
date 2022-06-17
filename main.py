import random

user_wins = 0
computer_wins = 0

moves = ["rock", "paper", "scissors"]

while True: 
  user_move = input("Type rock/paper/scissors or q to quit: ")  
  if user_move in ["rock", "paper", "scissors"]:
    computer_move = random.choice(moves)
    print("Computer move: ", computer_move)
    if user_move == "rock" and computer_move == "scissors":
      print("You win!")
      user_wins += 1
      continue
    elif user_move == "paper" and computer_move == "rock":
      print("You win!")
      user_wins += 1
      continue
    elif user_move == "scissors" and computer_move == "paper":
      print("You win!")
      user_wins += 1
      continue
    elif user_move == computer_move:
      print("Tie!")
      continue
    else:
      print("Computer wins.")
      computer_wins += 1
      
  elif user_move.lower() == "q":
   print("Quit Success:")
   break

  else:
    print("Invalid input, try again.")
    continue

print("Your # of games won =", user_wins)
print("Computer's # of games won =", computer_wins)