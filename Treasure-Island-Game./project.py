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

print("Welcome to the Treasure Island")
print("Your Missions is to find the Treasure")
option1 = input("You're at a crossroad, where do your want to go? Type Left or Right\n").lower()

if option1 == "left":
    option2 = input("You've come to a lake, There is an island in the middle of the lake. Type Wait for the boat. Type Swim to swim across").lower()
    if option2 == "wait":
        option3 = input("Your arrive at the island unharmed. There is a house with 3 doors. One red one blue and one yellow.Which Color do you choice?").lower()
        if option3 == "red":
            print("It's a room full of fire, Game Over")
        elif option3 == "yellow":
            print("You found the trousure, Your are Winner🎉🎉🎉")
        elif option3 == "blue":
            print("You enter a room of beasts. Sorry Game Over")
        else:
            print("Your choice a door don't exit. Game Over.")
    else:
        print("You Got Attacked by Angry Trout.Sorry Game Over")
else:
    print("You Fell into a hole, Game Over")
 



