rucksacks = open("day3/in.txt").read().strip().split('\n')
items = set()
total = 0
for rucksack in rucksacks:
    item = list((set(rucksack[:int(len(rucksack) / 2)]) & set(rucksack[int(len(rucksack) / 2):])))[0]
    if item.isupper():
        total += ord(item) - 65 + 27
    else:
        total += ord(item) - 96

print(total)
