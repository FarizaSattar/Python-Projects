# Treasure Island
''' The code presents an interactive text-based game where the user travels through adventure island. '''

# Prints ASCII art to console
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Opening Messages
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

# The user's first choice
choice1 = input('You\'re walking down a path and find yourself at a crossroad. Where do you want to go? Type "left" or "right" \n').lower()

# The user chose to go to the left
if choice1 == "left":
    
    # The user's second choice
    choice2 = input('You continue down the path and find yourself at a lake. You need to get to the island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across')
    
    # The user chose to wait
    if choice2 == "wait":
        
        # The user's third choice
        choice3 = input('You arrive at the island unharmed. You enter a house and find a hallway with 3 doors. They are red, yellow and blue. Which door do you choose?')
        
        # The user chose to enter the red room
        if choice3 == "red":
            print("Game over! You walk into a room full of fire!")
        
        # The user chose to enter the blue room
        elif choice3 == "blue":
            print("Game over! You walk into a room full of monsters!")
        
        # The user chose to enter the yellow room
        elif choice3 == "yellow":
            print("You win! You found the treasure!")
            
        # The user chose none of the above options
        else:
            print("Game over! You picked a door that does not exist!")
            
    # The user chose to swim 
    elif choice2 == "swim":
        print("Game over! You get attacked by an angry trout!")
        
    # The user chose none of the above options
    else:
        print("Game over! You chose to do nothing!")
        
# The user chose to go to the right
elif choice1 == "right":
    print("Game over! You fall into a hole!")

# The user chose none of the above options
else:
    print("Game over! You chose to do nothing!")