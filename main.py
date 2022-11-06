#Creating your Santa chat app XD
#This app will request the child for their name and tell them if they're on the nice or naughty list (50/50 chance)

### Steps ###
#Imports
import csv
import sys
import random

#takes in the child's name
name = input("Ho ho ho! Merry Christmas!\nMy name is Kris Kringle and I am the ambassador of the North Pole\nDear child, may I ask what your name is?\n").lower().strip()
while len(name) == 0:
  print(f"\nOh no, please try inputting your name!")
  name = input()


## Full List of Bad Words (Comma-Separated-Text-File)
#====================================

## This Full List of Bad Words is provided free by: Free Web Headers – https://www.freewebheaders.com

## Last Update: May 05, 2022

## URL: https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/

## Copy all the words below:
#----------------------------------

#Read the full list of bad words here


# opening the CSV file of all the bad words (credits above)
with open("full-list-of-bad-words_comma-separated-text-file_2022_05_05.csv", mode ='r') as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # If the name is on the curse word page
  fullset = set()
  for lines in csvFile:
    for i in lines:
      fullset.add(i)
  #print(fullset)
  if name in fullset:
    print("\nOH NO!!!!!!! \nYou have been automatially placed on the naughty list, \nan all time low \n>:( ")
    sys.exit()
file.close()



#Begin with default variables
uwu = False #Name not in csv files
naughty_or_nice = False #False = naughty list, default decision to be changed

#Read the more_easter_eggs_XD.csv file which is the good list

with open("more_easter_eggs_XD.csv") as files:
  csvFile = csv.reader(files)
  for lines in csvFile:
    if name in lines:
      print(f"\nDear {name}, you have made it to the nice list!")
      uwu = True #Name is in csv file, don't do random
      naughty_or_nice = True #Person in nice list
files.close()
#Read CSV file of easter_eggs_XD.csv for the people on the naughty list
with open("easter_eggs_XD.csv") as filess:
  csvFile = csv.reader(filess)
  for lines in csvFile:
    if name in lines:

      print(f"\nOh dear! My child, it appears you have fallen on the naughty list this year \n:(")
      uwu = True #Name is in csv file, don't do random
      naughty_or_nice = False #Person in naughty list
filess.close()


#If name is not in csv file, do random generator
if uwu == False:
  #Creating random list XD
  owo = random.choice([0,1])

  #If random number is 0, then they are on naughty list
  if owo == 0:
    print(f"\nOh dear! My child, it appears you have fallen on the naughty list this year \n:(")
    naughty_or_nice = False #Person in naughty list

  #If random number is 1, then they are on nice list
  else:
    print(f"\nDear {name}, you have made it to the nice list!")
    naughty_or_nice = True #Person in nice list


#If person in naughty list
if not naughty_or_nice:
  print(f"\n{name}, spreading kindness and holiday joy really should be your new goal. If you cannot turn your spirit around, you'll end up with a pile of coal \n:(")
  sys.exit()

#if person in nice list
else:
  print(f"\nThank you for spreading kindess and Christmas cheer!\nWhat would you like for Christmas this year? \n:) ")
  gift = input()

  #if person inputs nothing
  while len(gift) == 0:
    print(f"\nOh no, Dear {name}, please try inputting a gift idea!")
    gift = input()

  #if person inputs something in bad list
  if gift in fullset:
    print(f"\nUnfortunately, we don't accept bad words. Santa is very disappointed in your choice to use this language, so you have now been moved to the naughty list. You should tell your parents about this, and then reflect on your actions. Think long and hard about the person you one day want to become! \n:\\")
    sys.exit()

  #If person inputs a valid word
  else:
    print(f"\nOh my! What a wonderful, jovial, jolly gift idea!\nOur elves have been working hard to create something special for every person: no matter how near or far they may be.\nKeep that lovely holiday spirit going, and make sure to spread it to everyone you meet!\nHappy Holidays {name}!")
    sys.exit()
