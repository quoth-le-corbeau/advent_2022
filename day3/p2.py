rucksacks = open("day3/in.txt").read().strip().split('\n')
total = 0
for i, rucksack in enumerate(rucksacks):
    if i % 3 == 2:
        item = list(set(rucksacks[i]) & set(rucksacks[i - 1]) & set(rucksacks[i - 2]))[0]
        if item.isupper():
            total += ord(item) - 65 + 27
        else:
            total += ord(item) - 96

print(total)
