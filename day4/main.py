"""
https://adventofcode.com/2022/day/4
"""


points1:int = 0
points2:int = 0

# Calculation part.
with open("input.txt", "r") as f:
    for line in f:
        a,b = line.strip().split(",")
        a1, a2 = map(int, a.split("-"))
        b1, b2 = map(int, b.split("-"))
        x1 = set(range(a1, a2 + 1))
        x2 = set(range(b1, b2 + 1))
        if x1.issubset(x2) or x1.issuperset(x2):
            points1 += 1
        if x1 & x2:
            points2 += 1


# Solution for 1st question.
print(points1) # 413

# Solution for 2nd question.
print(points2) # 806