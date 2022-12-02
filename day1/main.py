# Day 1 of Advent of Code 2022
# Count Calories
# https://adventofcode.com/2022/day/1

# get input data
file = open("input.txt", "r")
data = file.read()
input = data.splitlines()

elves = []
calories = 0

for item in input:
    if item != "":
        calories += int(item)
    else:
        if calories > 0:
            elves.append(calories)
            calories = 0

#print("list of elves:" + str(elves))
print("highest calory elf: " + str(max(elves)))

top_x = 3
calories = 0
for i in range (0, top_x):
    current_max = max(elves)
    calories += current_max
    elves.remove(current_max)

print("top " + str(top_x) + " elves carry " + str(calories) + " calories in total.")