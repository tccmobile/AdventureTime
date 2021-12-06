import random
import time
import os

sonicPresent = True
inventory = []


def intro():
  print("DOCTOR WHO Adventure\n")
  print("The TARDIS slowly materializes on the planet.")
  print("\nThe Doctor steps out from the open door.")

def startPoint():
  print("-------------------")
  print("The empty field")
  print("-------------------")
  print("\nScanning the area, The Doctor sees a cave to the north,")
  print("a small house to the west and a wall to the east.")
  print("The TARDIS is behind him to the south")

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
      myChoice = myOptions("\nWhat do you want to explore? ","1) The house","2) The cave","3) Return to TARDIS","")

def gotoHouse():
  print("-------------------")
  print("The Ancient House") 
  print("-------------------")

  if "disruptor" in inventory:
    print("\nThere is an open and empty chest here.")
    print("There is nothing else of interest")
  else:
    print("\nThere is a locked chest here.") 
    if "sonic" in inventory:
      print("You use the sonic to open the chest")
      print("You find a frequency disrupter and pocket it.")
      inventory.append("disruptor")
    else:
      print("You see no way to open it")
  print("\nYou leave the house")
  startPath()


def gotoCave():
  print("-------------------")
  print("The Creepy Cave\n")
  print("-------------------")


def gotoTARDIS():
  global sonicPresent
  print("-------------------")
  print("Inside the TARDIS\n")
  print("-------------------")
  print("\nThe TARDIS console quietly hums.")
  if sonicPresent:
    print("\nYou see your sonic screwdriver.")
    pickup = input("Do you want to pick it up? (y/n)")
    if pickup == "y" or pickup == "Y":
        print("You pick up the sonic and stick it in your pocket")
        inventory.append("sonic")
        sonicPresent = False
    else:
      print ("Ok. There is nothing else to do.")
  else:
    print("\nYou see nothing of interest.")
  print("You leave the TARDIS")
  startPath()

def startPath():
  startPoint()
  choice = myOptions("\nWhat do you want to explore? ","1) The house","2) The cave","3) Return to TARDIS","")
  print("You chose option: ",choice)
  myPath(choice,gotoHouse,gotoCave,gotoTARDIS,None)

intro()
startPath()
