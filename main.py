import random
import time
import os

swordPresent = True
inventory = []


def intro():
  print("Cat Kingdom Python Adventure\n")
  print("")
  print("\n An Excellent Adventure.")

def startPoint():
  print("-------------------")
  print("The king's court")
  print("-------------------")
  print("\nThe brave knight stands at attention. There is")
  print("the king in front of him, a locked door to the west and east")
  print("and the outside door the south")

def myOptions(question, option1,option2, option3, option4):
  print(question)
  print(option1)
  print(option2)
  print(option3)
  print(option4)
  choice = input("\nWhat would you like to do? ")
  return choice

def myPath(myChoice, path1,path2,path3,path4):
  goodPath = False

  while not(goodPath):
    if myChoice == "1":
      path1()
      goodPath = True
    elif myChoice == "2":
      path2()
      goodPath = True
    elif myChoice == "3" and path3 != None:
      path3()
      goodPath = True
    elif myChoice == "4" and path4 != None:
      path4()
      goodPath = True
    else:
      print("I'm sorry I don't understand you! ")
      myChoice = input("Please enter only one of the numbers listed: ")

def gotoKing():
  print("-------------------")
  print("The Noble King") 
  print("-------------------")

  if "key" in inventory:
    print("\nYou have all I can give you.")
    print("Go start your adventure")
  else:
    print("\nBrave knight. You need to be equipped for the coming battle")
    print("Here is a key. Go to the armory and equip yourself")
    inventory.append("key")
  print("\nYou bow and leave the king's pressence")
  startPath()


def gotoYard():
  print("-------------------")
  print("The CourtYard\n")
  print("-------------------")
  print("Ahead is the outer gates to the castle")
  print("Behind is the king's court")
  choice = myOptions("\nWhat dost thou want to do? ","1) Leave the Outer Gates","2) Return to Castle","","")
  myPath(choice,gotoLand,startPath, None, None)

def gotoLand():
  print("You are eaten by a dragon")

def gotoKitchen():
  print("-------------------")
  print("The Kitchen\n")
  print("-------------------")

def gotoArmory():
  global swordPresent
  print("-------------------")
  print("The Armory\n")
  print("-------------------")
  print("\nThe sign of the door reads armory")
  if "key" in  inventory:
    print("You open the door and enter")
    if swordPresent:
      print("You see a magnificant sword")
      print("You arm yourself with it")
      inventory.append("sword")
      swordPresent = False
    else:
      print ("Their is nothing left in the armory")
  else:
    print("\nThe door is locked.")
  print("You step back from the door")
  startPath()

def startPath():
  startPoint()
  choice = myOptions("\nWhat dost thou want to do? ","1) Approach the King","2) Go to the Armory","3) Go to the Kitchen","4) Exit the Castle")
  print("You chose option: ",choice)
  myPath(choice,gotoKing,gotoArmory,gotoKitchen,gotoYard)

intro()
startPath()
