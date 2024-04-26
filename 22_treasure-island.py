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
print("Your mission is to find the treasure. \n") 

find_leave = input("It is a Mysterious Map! \n You find a worn map left by an old pirate. The map shows the location of the Treasure Island! What would you like to do? \n Type 'find' to find the treasure or 'leave' to leave the map and continue your journey. \n")
if find_leave == "find":
  trust_pass = input("You followed the map and it took you to the shore of the island. What is this? A boat is approaching. \n A drunk man came out of the boat and said he could take you to the treasure. What would you like to do? \n Type 'trust' to trust the old man or 'pass' to pass the boat. \n")
  if trust_pass == "pass":
    inside_pass = input("After passing the old man, you found a cave. What would you like to do? \n Type 'inside' to go inside into the cave or 'pass' to pass the cave. \n")
    if inside_pass == "inside":
      left_right_straight = input("Too dark! You are heading deeper into the cave and you come across a road that divides into three. Which one will you choose? \n Type 'left', 'right' or 'straight' to choose the direction. \n")
      if left_right_straight == "left":
        print("You have reached a fascinating cave filled with crystals. You saw a giant diamond in the center of the cave, reflecting the light of all the crystals. But looking at it, you probably didn't notice the skulls and human carcasses around. You run and take the diamond in your hands and at that moment you realize this. It's a trap. The stalactites above fall on your head and send you to eternity like the others. \n Game Over! \n")
      elif left_right_straight == "straight":
        print("You notice a small light shining in the darkness. As you moved towards the source of the light, you emerged in front of a hidden waterfall. Behind the waterfall, there is a room where the pirates hid the treasure. However, a key is required to open the door to the room. You notice something shining under the waterfall, and it's the missing key itself. You entered the room, there was dust everywhere, but you couldn't take your eyes off the sparkle of the treasure right in the middle of the room. You take the treasure, leave the cave and continue your life with wealth, but you are unaware of something... \n The curse of the treasure. \n")
      else:
        print("You have entered an abandoned mine tunnel. As you move through the tunnel, you see the marks left by old pirates on the walls. These show you the path that will lead you to the treasure. You continue looking at the walls and fall into a huge ditch. When you look around, you see the corpses of the treasure hunters who came before you, and at that moment you realize that you cannot get out of here. You are trapped in the ditch forever. \n Game Over!")
    else:
      print("You never found the treasure, but you continued to live your life happily, even though you were poor. \n")

  else:
    print("The old man turned out to be a human trader and is taking you to sell you as a slave in Egypt. \n Game Over! \n")

else:
  print("While you were walking on the road, Amerindians came across you and cooked you on a wood fire and ate you. \n Game Over! \n")