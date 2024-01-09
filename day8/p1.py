rows = open("day8/in.txt").read().strip().splitlines()
# print(rows)

visible_trees = []

for j, row in enumerate(rows):
    for i in range(len(row)):
        # outer rim
        if j == 0 or j == len(rows) - 1:
            visible_trees.append(row[i])
        # outer rim
        elif i == 0 or i == len(row) - 1:
            visible_trees.append(row[i])
        else:
            left = right = up = down = False
            # look left
            if all(int(row[x1]) < int(row[i]) for x1 in range(i)):
                left = True
            # look right!
            if all(int(row[x2]) < int(row[i]) for x2 in range(i + 1, len(row))):
                right = True
            # look up
            if all(int(rows[y1][i]) < int(row[i]) for y1 in range(j)):
                up = True
            # look down
            if all(int(rows[y2][i]) < int(row[i]) for y2 in range(j + 1, len(rows))):
                down = True
            if left or right or up or down:
                visible_trees.append(row[i])

print(len(visible_trees))
