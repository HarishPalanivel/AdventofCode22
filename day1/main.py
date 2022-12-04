"""
https://adventofcode.com/2022/day/1
"""

# Calculate calories carried by elves.
with open("input.txt", "r") as f:
    total_calorie_list = []
    calorie_of_elf: int = 0
    for line in f:
        if line == "\n":
            total_calorie_list.append(calorie_of_elf)
            calorie_of_elf = 0
        else:
            calorie_of_elf += int(line)

# Solution for 1st question.
print(max(total_calorie_list)) # 71023

#Solution for 2nd question.
print(sum(sorted(total_calorie_list, reverse=True)[:3])) # 206289