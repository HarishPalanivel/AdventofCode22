with open("day1\\input.txt", "r") as f:
    total_calorie_list = []
    calorie_of_elf: int = 0
    for line in f:
        if line == "\n":
            total_calorie_list.append(calorie_of_elf)
            calorie_of_elf = 0
        else:
            calorie_of_elf += int(line)
    print(max(total_calorie_list))
    print(sum(sorted(total_calorie_list, reverse=True)[:3]))