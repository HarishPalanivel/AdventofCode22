rps: dict = {"A X": 4, "A Y" : 8, "A Z" : 3, "B X": 1, "B Y": 5, "B Z" : 9, "C X": 7, "C Y": 2, "C Z" : 6}
rps2: dict = {"A X": 3, "A Y" : 4, "A Z" : 8, "B X": 1, "B Y": 5, "B Z" : 9, "C X": 2, "C Y": 6, "C Z" : 7}
points: int = 0
points2: int = 0
with open("input.txt", "r") as f:
    for line in f:
        filter = line.strip()
        points += rps[filter]
print(points)

with open("input.txt", "r") as f:
    for line in f:
        filter = line.strip()
        points2 += rps2[filter]
print(points2)
