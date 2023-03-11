import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
if(user_choice) == "0":
  print(rock)
elif(user_choice) == "1":
  print(paper)
elif(user_choice) == "2":  
  print(scissors)
else:
  print("Wrong Choice")

print("Computer Choice: ")
option = ("rock", "paper", "scissors")
random_game = random.choice(option)

if random_game == "rock":
  print(rock)
elif random_game == "paper":
  print(paper)
else:
  print(scissors)

if user_choice == "0" and random_game == "rock":
  print("Win Win")
elif user_choice == "1" and random_game == "paper":
  print("Win Win")
elif user_choice == "2" and random_game == "scissors":
  print("Win Win")
elif user_choice == "0" and random_game == "paper":
  print("You Lose")
elif user_choice == "0" and random_game == "scissors":
  print("You Win")
elif user_choice == "1" and random_game == "rock":
  print("You Win")
elif user_choice == "1" and random_game == "scissors":
  print("You Lose")
elif user_choice == "2" and random_game == "rock":
  print("You Lose")
elif user_choice == "2" and random_game == "paper": 
  print("You Win")
