"""
https://adventofcode.com/2022/day/2
"""


def points_cal(path: str, predicted_result: dict):
    """Calculates the points based on the input and the possible outcomes of each play."""
    points:int = 0
    with open(path, "r") as f:
        for line in f:
            points += predicted_result[line.strip()]
    return points


# Possible outcomes for each play and the points awared, for both questions.
rps: dict = {"A X": 4, "A Y" : 8, "A Z" : 3, "B X": 1, "B Y": 5, "B Z" : 9, "C X": 7, "C Y": 2, "C Z" : 6}
rps2: dict = {"A X": 3, "A Y" : 4, "A Z" : 8, "B X": 1, "B Y": 5, "B Z" : 9, "C X": 2, "C Y": 6, "C Z" : 7}


#Solution for 1st question.
print(points_cal("input.txt", rps)) # 8890

#Solution for 2nd question.
print(points_cal("input.txt", rps2)) # 10238