"""
Programmer: Ryan Lee

This program is a simple game meant to test reaction speed. Instructions are provided upon running the code.

The program will automatically record the results in a list that can be easily viewed outside of the trials, and uses a threshold time to prevent accidental
early inputs from skewing the resulting data. 

I hope any who use this code have fun!
"""

import time
import random

# Introductory text that provides info about how to use this program to the viewer
intro_text = "Hello! This program will test your reaction time.\nBefore typing, please read the following information carefully: \n \
1. If you wish to quit, please type 'quit' and press enter \n 2. When the test begins, there will be a pause that lasts anywhere from 1-10 seconds, \
followed by a bunny (to see the bunny outside of tests, type 'bunny') appearing on screen.\n When you see the bunny, press enter as soon as possible \n \
3. Your time will be printed on the screen, and all of your results from this session will be stored in a list.\
    \n   To view the list, please type 'view' \n \
5. To begin the test, type 'start' \n 6. Finally, for a list of all available commands, type 'help'"

# A list of commands that can be printed with the right keyword
commands = "To quit: 'quit' \n To start the test: 'start' \n To view previous times: 'view' \n To view the bunny: 'bunny' \n To view the commands: 'help'"

# Just a cute style choice
# Acts as the trigger message for the test
# Large enough to be easily visible to the viewer when printed
bunny = "\
|-----------| \n\
| NOW!!!    | \n\
|-----------| \n\
(\__/) || \n\
(•ㅅ•) || \n\
/ 　 づ "

# Will store user input for later
value = ""
# Will track how many times the test has been run
counter = 0
# List to store all previous times
times = []
# Holds the number of seconds to wait before printing the bunny
wait = 0
# Checks time when bunny is printed
start = 0
# Checks time when user reaction is recorded
end = 0
# Amount of time (in seconds) it took to react 
speed = 0
# Threshold: If overall time is < threshold, the likelihood of cheating (providing input before bunny appears) is
#            high, so the time will be deleted and another trial will run
# Note: Threshold is based on the time it takes for light stimuli to reach the brain 
threshold = 0.1

print(intro_text)
while value != "quit" :
    value = input().lower()
    if value == "help":
        print(commands)
    elif value == "view":
        print(times)
    elif value == "bunny":
        print(bunny)
    elif value == "start":
        print("How many times would you like to run the test?")
        print("Note: Please only input integers")
        count = int(input("Number: "))
        x = 0
        while x < count:
            print("Beginning...\n")
            time.sleep(2)
            print("GET READY!\n")
            wait = random.randint(1, 10)
            time.sleep(wait)
            print(bunny)
            start = time.time()
            if input() != None:
                end = time.time()
                speed = end - start
                if speed < threshold:
                    print("WARNING: Possible cheating detected \n Please do not provide input before bunny appears. \n This trial will be restated.\n")
                    time.sleep(1)
                else:
                    x += 1
                    counter += 1
                    times.append((speed))
                    print(f"Your time was: {speed}")
                    print(f"The program has been run {counter} times \n")
            # Refresh value to prevent bugs like the above commands running in between trials
            value = ""
        print(f"{count} trials completed")

