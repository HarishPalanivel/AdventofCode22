"""
https://adventofcode.com/2022/day/3
"""

def priority(character: str):
    # Takes a character and returns its priortity according to the challenge.
    ascii_index = ord(character)
    if ascii_index >= 97:
        return ascii_index - 96
    else:
        return ascii_index - 38

def common_in_comp(rucksack: str):
    # Returns the common character among the given input, which is the 2 compartments of an elf.
    midpoint = int(len(rucksack.strip()) / 2)
    comp_1,comp_2 = rucksack[:midpoint], rucksack[midpoint:]
    for i in comp_1:
        for j in comp_2:
                if i == j:
                    return i

def common_in_group(group: list):
    # Returns the common character among the given input, which is the group of 3 elfs.
    ind_1,ind_2,ind_3 = group[0], group[1], group[2]
    for i in ind_1:
        for j in ind_2:
            for k in ind_3:
                if i == j == k:
                    return i


points1: int = 0
points2: int = 0

# Solution for 1st question.
with open("input.txt", "r") as f:
    for line in f:
        points1 += priority(common_in_comp(line))

print(points1) # 8176


# Solution for 2nd question.
with open("input.txt", "r") as f:
    index: int = 0
    groups = []
    individuals = []
    for line in f:
        if index < 2:
            individuals.append(line)
            index += 1
        else:
            individuals.append(line)
            index = 0
            groups.append(individuals)
            individuals = []
            
for group in groups:
    points2 += priority(common_in_group(group))
print(points2) # 2689