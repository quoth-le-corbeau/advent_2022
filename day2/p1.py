# Rock: 1, 24
# Paper: 2, 25
# Scissors: 3, 26

# Wins: Rock: 24 - 3 = 21, Paper: 25 - 1 = 24, Scissors: 26 - 2 = 24 => {21, 24}
# Draws: Rock: 24 - 1 = 23, Paper: 25 - 2 = 23, Scissors: 26 - 3 = 23 => {23}
# Losses: Rock: 24 - 2 = 22, Paper: 25 - 3 = 22, Scissors: 26 - 1 = 25 => {22, 25}

games = open("day2/in.txt").read().strip().split('\n')
score = 0
for game in games:
    me = ord(game[2]) - 64
    score += me - 23
    elf = ord(game[0]) - 64
    decider = me - elf
    if decider in [21, 24]:
        score += 6
    elif decider == 23:
        score += 3
    else:
        continue

print(score)
