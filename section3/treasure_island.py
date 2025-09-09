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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are walking along a deserted path. You come to a fork in this path.")
direction = input("Do you go left or right?\n").lower()
if direction == "left":
  print("You walk along a quiet path for some time and can soon hear the sound of water. You come to a large river.")
else:
  print("You are attacked by a pack of wolves and die. Game Over.")
  
if direction == "left":
  river = input("Do you wait for the ferry or try to swim across? Type wait or swim.\n").lower()
  if river == "wait":
    print("You wait patiently for the ferry and are able to safely travel across the river.")
  if river == "swim":
    print("You try to swim across but you feel a skeletel hand grab your leg and slowly pull you down into the depths. Game Over.")

  if river == "wait":
    print("Once on the other side of the river you come to a town. You decide to get a room at the inn to rest for a while. The innkeeper tells you to pick any room.\nOnce upstairs, you find three doors, one red, one blue and one yellow. You must choose one to enter.")
    room = input("Which do you choose? Type red, blue or yellow.\n").lower()
    if room == "red":
      print("You encounter a room full of bandits hiding out. They kill you and take all of your gear. Game Over.")
    elif room == "blue":
      print("You open the blue door and walk into the room. Unfortunately, this room is in need of repairs and you fall through the broken floor into a giant pit full\nof broken rocks and boards. You sadly break your neck and die. Game Over.")
    else:
      print("You enter the room with the yellow door and find the most luxurious bed, where you lie down and fall into the most restful sleep you can ever remember having. \nCongratulations, you have found the treasure: the best night\'s sleep anyone could ever want. You Win!")