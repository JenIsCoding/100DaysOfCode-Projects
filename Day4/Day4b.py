# Rock Paper & Scissors Game

import random

rock = r'''
                _ 
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
'''

paper = r'''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        
'''

scissors = r'''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
'''

combination = [rock, paper, scissors]

user_comb = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(combination[user_comb])

pc_comb = random.randint(0,2)
print("Computer choose:")
print(combination[pc_comb])

if user_comb == 0 and pc_comb == 2:
    print("You win!")
elif user_comb == 2 and pc_comb == 0:
    print("You lose.")

if user_comb == 2 and pc_comb == 1:
    print("You win!")
elif user_comb == 1 and pc_comb == 2:
    print("You lose.")


if user_comb == 1 and pc_comb == 0:
    print("You win!")
elif user_comb == 0 and pc_comb == 1:
    print("You lose.")
else:
    print("It\'s a draw!")