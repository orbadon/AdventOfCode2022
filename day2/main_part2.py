# Day 2 of Advent of Code 2022
# Rock Paper Scissors - Part 2
# https://adventofcode.com/2022/day/2

# get input data
file = open("input.txt", "r")
data = file.read()

# Opponent:  A = Rock, B = Paper, C = Scissors
# Outcome:   X = Lose, Y = Draw, Z = Win
# Points:    Rock = 1, Paper = 2, Scissors = 3
#            Lose = 0, Draw = 3, Win = 6

# Convert ABC to Rock Paper Scissors because I can
data = data.replace("A", "Rock").replace("B", "Paper").replace("C", "Scissors")
# Convert XYZ to Lose, Draw, Win
data = data.replace("X", "Lose").replace("Y", "Draw").replace("Z", "Win")

games = data.splitlines()

game_score = {"Lose": 0, "Draw": 3, "Win": 6}
hand_score = {"Rock": 1, "Paper": 2, "Scissors": 3}

required_hand = {"Win": {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"},
                 "Draw": {"Rock": "Rock", "Paper": "Paper", "Scissors": "Scissors"},
                 "Lose": {"Paper": "Rock", "Scissors": "Paper", "Rock": "Scissors"}}

total_score = 0

for game in games:
    opponent_hand, game_outcome = game.split()
    score = 0
    score += game_score[game_outcome]
    my_hand = required_hand[game_outcome][opponent_hand]
    score += hand_score[my_hand]
    print("Opponent plays '" + opponent_hand + "', I need to '" + game_outcome + "' therefore I play '" + my_hand + "'. Game score: " + str(score))
    total_score += score

print("Total score: " + str(total_score))
