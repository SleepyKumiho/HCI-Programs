"""
Writing out main thoughts for now. Will be deleted later as code is written

Use a while loop to keep the prgram running as long as desired, with a kill condition using input

input()

have the kill condition activate on q or quit or kill,  whatever you want
have a randint function choose a random number, have the code pause for that many seconds, and then print out a large whatever, as long as it is clearly visible

  maybe the bunny holding a sign that says "NOW!!!"
  
 upon pressing enter the clock will record the time, print it to the screen, and store it in a list. 
The name of the list will also be given, and the number of times the program has been used in this session will be printed for the sake of the user
Add an input funcftion "view" to get the listed times all printed to the screen.

Likely need to add multiple input conditions using if statements for this to work

Possible food for thought: If the user presses enter too early, how do we stop them?
  Until this is programmed in, add to the starting text blurb saying: hey, we trust you not to cheat right now
"""

import time
import random

# Introductory text that provides info about how to use this program to the viewer
intro_text = "Hello! This program will test your reaction time.\n Before typing, please read the following information carefully: \n \
1. If you wish to quit, please type 'quit' and press enter \n 2. When the test begins, there will be a pause that lasts anywhere from 1-10 seconds, \
followed by a bunny appearing on screen.\n   When you see the bunny, press enter as soon as possible \n \
3. Your time will be printed on the screen, and all of your results from this session will be stored in a list.\
    \n   To view the list, please type 'view' \n \
5. To begin the test, type 'start' \n 6. Finally, for a list of all available commands, type 'help'"

# A list of commands that can be printed with the right keyword
commands = "To quit: 'quit' \n To start the test: 'start' \n To view previous times: 'view' \n To view the commands: 'help'"

print(intro_text)

# Will store user input for later
value = ""
# Will track how many times the test has been run
counter = 0
# List to store all previous times
times = []

# The interactive portion
while value != "quit" :
    value = input().lower()
    if value == "help":
        print(commands)
    elif value == "view":
        print(times)
    elif value == "start":
        counter += 1
        print("Not implemented")
        times.append(random.randint(1, 10))
        print(f"The program has been run {counter} times")
