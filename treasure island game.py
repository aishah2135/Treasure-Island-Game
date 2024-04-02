# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:19:00 2024

@author: aisha
"""
print("Welcome to Treasure Island!")
print("Your goal is to find the hidden treasure chest.")

print('''  
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right". ' ).lower() #accepts upper or lowercase 

if choice1 == "left": 
    choice2 = input('You\'ve come to a lake. There is a island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim across. ').lower()
    if choice2 == "wait":
       choice3 = input('You\'ve arrive at the island safely. Now there is a house with 3 doors. A red door, a blue door, and a yellow door. Which door do you choose? ').lower()
    if choice3 == "red": 
        print("You have found a room full of angry cobras. Game Over.")
    elif choice3 == "yellow": 
        print("Congratulations!!! You found the treasure. You win!")
    elif choice3 == "blue": 
        print("You have found a room full of angry gorillas. Game Over.")
    else: 
      print("You were attacked by a hungry alligator. Game Over.")
else: 
   print("You fell into a pit. Game Over.")
       

