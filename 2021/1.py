import numpy as np
from aocd.models import Puzzle

def parses(text):
    return np.array([int(i) for i in text.strip().split("\n")])

def count_larger(nums):
    count = 0
    if len(nums) >= 2:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count+=1
    return count

def n_sum(n, nums):
    sum_list = []
    for i in range(n-1, len(nums)):
        sum_list.append(sum(nums[i-n+1:i+1]))
    return sum_list


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=1)
    data = parses(puzzle.input_data)
    cl = count_larger(data)
    cl_3 = count_larger(n_sum(3, data))
    print(cl)
    print(cl_3)
    #puzzle.answer_a = #INSERT PART 1 ANSWER
    #puzzle.answer_b = #INSERT PART 2 ANSWER