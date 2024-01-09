# winner points (elf: me):
# 1: 2
# 2: 3
# 3: 1

# lose points (elf: me):
# 1: 3
# 2: 1
# 3: 2


games = open("day2/in.txt").read().strip().split('\n')
score = 0
for game in games:
    me = ord(game[2]) - 64
    lose = me == 24
    draw = me == 25
    win = me == 26
    elf = ord(game[0]) - 64
    if draw:
        score += elf + 3
    elif win:
        winner = elf + 1
        if winner == 4:
            winner = 1
        score += winner + 6
    elif lose:
        loser = (elf + 2) % 3
        if loser == 0:
            loser = 3
        score += loser

print(score)
