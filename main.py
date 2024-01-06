# 9.1 The Text Adventure
# L Ren
# Mar 25, 2021
# https://replit.com/@LeonRen2/91-The-Text-Adventure

# import module
from os import system, name
import random

# global variables
doorslist = [1,2]

# functions
def clear_the_screen(): # clears the screen
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

def show_the_screen(): # header and says text adventure game
  print("______________ Text Adventure Game ______________")
  
def plot(): # describes the story to the user 
  print()
  print("| imagine this . . . |")
  print("-------------------------------------------------")
  print("you are hiking on a mountain. you become exhausted, so you lie down underneath a tree to take a nap. your eyes are droopy and you finally fall asleep.")
  print("-------------------------------------------------")
  print("suddenly, you wake up and find yourself you're in a dark room. you realize that you've been abducted and the only way to survive is to pass a series of obstacles. ")
  print("-------------------------------------------------")
  print()
  input("press enter key to proceed: ")

def game(): # this is the game and the user answers questions and gets results
  print("the objective of the game is to live. if you lose, you die. this adventure will unravel and branch out into many scenarios. if you lose or win the game, just press restart or run to play again. to start this game, please answer these questions: ")
  print("* note: after answering each question, press enter key to continue *")
  print("-------------------------------------------------")
  ip = input("who is the most important person in your life? " ) # first question
  fear = input("what is your greatest fear? ") # second question
  print()
  print("now, let's start!")
  print("suddenly, two doors emerge from a wall: a left one and a right one")
  print()
  print("(1) left door")
  print("(2) right door") 
  print()
  doors = input("which do you pick (1/2)? ").strip()
  print("-------------------------------------------------")
  if doors == str(doorslist[0]): # first door aka left 
    print("you enter a new room. you notice that your shoes are wet and the water is rising! there are two buttons and you have to press one of them.")
    print()
    print("(1) blue button")
    print("(2) red button") 
    print()
    colorbuttons = input("which color button do you choose (1/2)? ").strip()
    print("-------------------------------------------------")
    if colorbuttons == "1": 
      print("you see two objects to aid you from drowning: a shovel or a large bucket.")
      print()
      print("(1) shovel")
      print("(2) large bucket") 
      print()
      objects = input("which object do you choose (1/2)? ").strip()
      print("-------------------------------------------------")
      if objects == "1":
        print("you start digging in the ground and realize there's a door in the ground. you open it and all the water starts rushing into the ground and you can finally breathe.")
        print("there are two tunnels in front of you: a left tunnel and a right tunnel.")
        print()
        print("(1) left tunnel")
        print("(2) right tunnel") 
        print()
        tunnels = input("which tunnel do you choose (1/2)? ").strip()
        print("-------------------------------------------------")
        if tunnels == "1":
          print("you walk in the tunnel and see " + ip + " tied with handcuffs. some items appear again that could potentially be useful.")
          print()
          print("(1) an unknown colored button")
          print("(2) bobby pin") 
          print("(3) ax") 
          print()
          secondobject = input("which second object do you choose (1/2/3)? ").strip()
          print("-------------------------------------------------")
          if secondobject == "1": # survived
            print("you took a chance . . . and you lived! the button released " + ip + ". and, a path took you two back to the mountain trail. you win!")
          elif secondobject == "2": # died
            print("sadly, you don't know how to pick the cuffs and you two starved and died. you lose.")
          elif secondobject == "3": # died
            print("while attempting to remove the cuffs, you accidentally chop off " + "'s hands and cut your leg. you both bleed out and die. you lose.")
          else:
            print("error: not a choice")
        elif tunnels == "2": # died 
          print("a pit is located in the center of the tunnel you accidentally fall to you death. you lose.")
        else:
          print("error: not a choice")
      elif objects == "2": # died
        print("you tried to scoop up some of the water. unfortunately, there was too much water and you died. you lose.")
      else:
        print("error: not a choice")
    elif colorbuttons == "2":
      print("you see two objects to aid you from drowning: an ax or an oxygen tank. choose one")
      print()
      print("(1) ax ")
      print("(2) oxygen tank") 
      print()
      objects_r1 = input("which object do you choose (1/2)? ").strip()
      print("-------------------------------------------------")
      if objects_r1 == "1":
        print("you start digging into the walls, which leads you and the water out of the room. and, you can now breathe.")
        print("after some time, you see two tunnels in front of you: a left tunnel and a right tunnel.")
        print()
        print("(1) left tunnel")
        print("(2) right tunnel") 
        print()
        tunnels_r1 = input("which tunnel do you choose (1/2)? ").strip()
        print("-------------------------------------------------")
        if tunnels_r1 == "1": # survived 
          print("the path led to back to nature and you survived! you win!")
        elif tunnels_r1 == "2": # death
          print("waiting for you at the end of the tunnel was your fear: " + fear + ". the fear triggers a panic attack. you lose.")
        else:
          print("error: not a choice")
      elif objects_r1 == "2": # death
        print("the oxygen tank only gave a brief moment of relief and air. the oxygen eventually ran out and you died. you lose.")
      else: 
        print("error: not a choice")
    else: 
      print("error: not a choice")
  elif doors == str(doorslist[1]): # second door aka right 
    print("you enter a new room. you notice that you're sweating and your skin is starting to blister. you're in an oven room! there are two buttons and you have to press one of them.")
    print()
    print("(1) blue button")
    print("(2) red button") 
    print()
    colorbuttons2 = input("which color button do you choose (1/2)? ").strip()
    print("-------------------------------------------------")
    if colorbuttons2 == "1":
      print("the temperature of the room to drops back to normal and you recieve vision goggles.")
      print("you put them on and find that there is a vent that could perphaps lead you to safety. as you're crawling in the vent, the path diverges into two sections: left vent and right vent")
      print()
      print("(1) left vent")
      print("(2) right vent") 
      print()
      vent = input("which vent do you choose (1/2)? ").strip()
      print("-------------------------------------------------")
      if vent == "1": # death
        print("inside the left vent, there is/are your fear: " + fear + ". the fear triggers a panic attack. you lose." )
      elif vent == "2": # survived
        print("as you crawl in the right vent, it slides into a tunnel where you're reunited with " + ip + ". you two crawl out and live! you win!")
      else:
        print("error: not a choice")
    elif colorbuttons2 == "2": # death
      print("you recieve gallons of water. however, due to the extreme heat of the room, it evaporates and you die of hydration. you lose.")
    else:
      print("error: not a choice")
  else:
    print("error: not a choice")

def play_the_game(): # components of the game and controls each function
  clear_the_screen()
  show_the_screen()
  while (True): 
    plot()
    clear_the_screen()     
    game()
    break
  
# start here
play_the_game() # plays the game 