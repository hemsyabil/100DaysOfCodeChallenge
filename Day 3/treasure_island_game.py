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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************      
''')
print("Welcome to Treasure Island. Your mission is to find the treasure")

user_input = input("You are at the cross road. \nWhere do you wan to go? \n type 'Left' or 'Right'")

if user_input.lower() == 'right':
    print("You fall into the hole. Game Over!")
    exit()
else:
    print("You have come to a lake. There is an island in the middle of the lake.")
    user_input = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.")

    if user_input.lower() == 'wait':
        print("You arrived at the island unharmed. There is a house with three doors.")
        user_input = input("One red, one yellow, and one blue. Which color will you choose?")

        if user_input.lower() == 'red':
            print("You are burned by the fire. Game Over!")
            exit()
        elif user_input.lower() == 'blue':
            print("You are eaten by beasts. Game Over!")
            exit()
        elif user_input.lower() == 'yellow':
            print("You found the treasure! Congratulations!")
            exit()
        else:
            print("You chose an invalid color. Game Over!")
            exit()
    else:
        print("You get attacked by a trout. Game Over!")
        exit()
