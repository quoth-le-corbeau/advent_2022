elves = [0]
totals = []
while True:
    try:
        calories = input()
    except:
        break
    if calories == "":
        totals.append(sum(elves))
        elves = [0]
    else:
        elves.append(int(calories))

print(max(totals))

