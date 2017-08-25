# DS 6001: Homework 1
# Simulate the Monty Hall Problem
# Group 8
# Elizabeth Homan: Leader/Coordinator
# Gregory Wert: Researcher
# Xinyang Liu: Coder

import random

def simulate(num_door, switch):
    # Place the car behind a random door
    car_door = random.randint(0, num_door - 1)
    # Choose a door
    choice = random.randint(0, num_door - 1)
    # Create a list of all closed doors
    closed_door = list(range(num_door))
    # Write a while loop to make sure that 2 doors are left closed
    while len(closed_door) > 2:
        # Open a random door
        open_door = random.choice(closed_door)
        # Make sure that the opened door is neither the car_door nor the choice
        if open_door == car_door or open_door == choice:
            continue
        closed_door.remove(open_door)
    # Whether the constestant choose to switch the door
    if switch:
        # The only door that will be left closed at the end will the door other than contestant's initial choice
        closed_door.remove(choice)
        choice = closed_door.pop()
    # Whether the contestant wins
    win = 0
    if choice == car_door:
        win = 1
    return win

switch_win = 0
stay_win = 0
# Run the simulation for 10,000 times for each case
for i in range(0, 10000):
    # The number of times the contestant wins if switch
    switch_win += simulate(3, True)
    # The number of times the contestant wins if don't switch
    stay_win += simulate(3, False)
print("The probability of winning if the contestant switch " + str(switch_win / 10000))
print("The probability of winning if the contestant does not swtich " + str(stay_win / 10000))