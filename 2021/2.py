import numpy as np
from aocd.models import Puzzle

def parses(text):
    return np.array([i for i in text.strip().split("\n")])

if __name__ == "__main__":
    #Part A
    puzzle = Puzzle(year=2021, day=2)
    depth = 0
    horiz = 0
    for movement in parses(puzzle.input_data):
        info = movement.split(" ")
        direction = info[0]
        mag = int(info[1])
        if direction == "forward":
            horiz += mag
        elif direction == "up":
            depth -= mag
        else:
            depth += mag
        
    print("A answer:", depth*horiz)

    #Part B
    puzzle = Puzzle(year=2021, day=2)
    depth = 0
    horiz = 0
    aim = 0
    for movement in parses(puzzle.input_data):
        info = movement.split(" ")
        direction = info[0]
        mag = int(info[1])
        if direction == "forward":
            horiz += mag
            depth += aim*mag
        elif direction == "up":
            aim -= mag
        else:
            aim += mag
    print("B answer:",depth*horiz)
