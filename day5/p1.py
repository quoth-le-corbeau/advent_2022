from collections import defaultdict

lines = open("day5/in.txt").read().split("\n")

rows = []
count = 0
for line in lines:
    if line == "":
        break
    rows.append([line[1::4]])
    count += 1

rows = rows[:-1]

stacks = defaultdict(list)
for row in rows:
    assert len(row) == 1
    for x in range(len(row[0])):
        if row[0][x] == " ":
            continue
        else:
            stacks[str(x + 1)].append(row[0][x])

for stack in stacks.values():
    stack.reverse()

for i in range(count + 1, len(lines) - 1):
    instruction = lines[i].split()
    n = int(instruction[1])
    # stacks[instruction[-1]].extend(stacks[instruction[3]][-n:][::-1])
    stacks[instruction[-1]] += (stacks[instruction[3]][-n:][::-1])
    stacks[instruction[3]] = stacks[instruction[3]][:-n]

solution = ""
for j in range(len(stacks)):
    solution += stacks[str(j + 1)][-1]

print(solution)

