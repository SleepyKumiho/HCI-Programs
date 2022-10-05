import time
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
print("Hello! This program will test your reaction time.")
print("Before typing, please read the instructions carefully:")
print("  1. If you wish to quit, please type 'q' and press enter")
print("  2. When the test begins, there will be a pause that lasts anywhere from 0-10 seconds, \
followed by a bunny appearing on screen. When you see the bunny, press enter as soon as possible.")
print("  3. Your time will be printed on the screen, and all of your results from this session will be stored in a list")
print("  4. To view the list, please type 'view'")
print("  5. Finally, to begin the test, type 'start'")
