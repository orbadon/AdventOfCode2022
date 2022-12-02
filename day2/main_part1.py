# Day 2 of Advent of Code 2022
# Rock Paper Scissors
# https://adventofcode.com/2022/day/2

# get input data
file = open("input.txt", "r")
data = file.read()

# Opponent:  A = Rock, B = Paper, C = Scissors
# Me:        X = Rock, Y = Paper, Z = Scissors
# Points:    Rock = 1, Paper = 2, Scissors = 3
#            Lose = 0, Draw = 3, Win = 6

# Convert XYZ to ABC
data = data.replace("X", "A").replace("Y", "B").replace("Z", "C")
# Convert ABC to Rock Paper Scissors because I can
data = data.replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors")

games = data.splitlines()

def game_score(opponent, me):
    if opponent == me:
        return 3
    elif ((opponent == "Rock" and me == "Scissors") or
          (opponent == "Paper" and me == "Rock") or
          (opponent == "Scissors" and me == "Paper")):
        return 0
    else:
        return 6

hand_score = {"Rock": 1, "Paper": 2, "Scissors": 3}

total_score = 0

for game in games:
    opponent_hand, my_hand = game.split()
    score = 0
    score += hand_score[my_hand]
    score += game_score(opponent_hand, my_hand)
    print("Opponent plays '" + opponent_hand + "', I play '" + my_hand + "'. Game score: " + str(score))
    total_score += score

print("Total score: " + str(total_score))
