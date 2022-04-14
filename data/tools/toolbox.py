import os, sys, math, random, time
from termcolor import colored
from pyfiglet import Figlet
 

from pprint import pprint

 

clear = lambda: os.system('cls')

 

def typingPrint(text):

  for character in text:

    sys.stdout.write(character)

    sys.stdout.flush()

    time.sleep(0.05)

  sys.stdout.write('\n')

def slowTypingPrint(text):

  for character in text:

    sys.stdout.write(character)

    sys.stdout.flush()

    time.sleep(0.05)

  sys.stdout.write('\n')

 

def typingInput(text):

  for character in text:

    sys.stdout.write(character)

    sys.stdout.flush()

    time.sleep(0.05)

  value = input()  

  return value  

 

intro = {

    "1" : [
      {"A" : "this is the first statement.A", 1 : 2},
      {"B" : "this is the second statement.B", 3 : 4},
      {"C" : "this is the third statement.C", 5 : 6},
      {"D" : "this is the third statement.D", 5 : 6},
     ],

    "2" : [
      {"A":"This is the first statement, of the second text block."},
      {"C":"This is the second."},
      {"B":"Third."}
    ]

}

 

def textBlock(statement, filter):

    clear()

    for index in statement:
      textloop(index, filter)

    typingInput('>')
    clear()

 

def textloop(index, filter):
  
  for item in index:
    if item == filter:

        typingPrint(str(index[item]))

    elif item == "B":

        time.sleep(2)

        typingPrint(index[item])

    elif item == "C":

        time.sleep(1)
        slowTypingPrint(index[item])

# clear()

# typingPrint('hello world')

# typingInput('>')

# clear()

 

for key, values in intro.items():

  textBlock(values, 1)

 

# dataList = [{'a': 1}, {'b': 3}, {'c': 5}]

# for dic in dataList:

#     for key in dic:

#         print(dic[key])