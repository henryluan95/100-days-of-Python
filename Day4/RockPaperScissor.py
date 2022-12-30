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


import random;

optionList = [rock, paper, scissors]

playerChoice = int(input("What do you choose? Type 0 or Rock, 1 for Paper or 2 for Scissor.\n"))

print(optionList[playerChoice])

computerChoice = random.randint(0,2)

print("Computer chose:")
print(optionList[computerChoice])

if(playerChoice == 0 and computerChoice == 1):
  print("You lose!")
elif(playerChoice == 0 and computerChoice == 2):
  print("You win!")

if(playerChoice == 1 and computerChoice == 0):
  print("You win!")
elif(playerChoice == 1 and computerChoice == 2):
  print("You lose!")

if(playerChoice == 2 and computerChoice == 0):
  print("You lose!")
elif(playerChoice == 2 and computerChoice == 1):
  print("You win!")

if(playerChoice == computerChoice):
  print("Draw!")

print("Hello")