# Take the input stream. 
with open("input.txt", "r") as f:
    stream = f.read()


# Solution for Part 1. 
last_four_char = ""
for i in range(1, len(stream)): # Assuming we will find the answer, well before the entire length of stream is checked.
    last_four_char = stream[i: i+4]
    if (len(last_four_char) == len(set(last_four_char))):
        print("Last four received characters : ", str(last_four_char)) # lhtw
        print("Start-Of-Packet marker appears at ", str(i + 4)) # 1909
        break

print()

# Solution for Part 2. 
last_fourteen_char = ""
for j in range(1, len(stream)): # Assuming we will find the answer, well before the entire length of stream is checked.
    last_fourteen_char = stream[j: j+14]
    if (len(last_fourteen_char) == len(set(last_fourteen_char))):
        print("Last fourteen received characters : ", str(last_fourteen_char)) # hndbzfswtmvcpr
        print("Start-Of-Message marker appears at ", str(j + 14)) # 3380
        break
