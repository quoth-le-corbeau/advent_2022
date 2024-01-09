rows = open("day8/test_in.txt").read().strip().splitlines()

for j, row in enumerate(rows):
    for i, tree in enumerate(row):
        left_count = right_count = up_count = down_count = 0
        tree = int(tree)
        a = b = i
        c = d = j
        # Left
        while a >= 0:
            if tree > int(row[a]):
                left_count += 1
            a -= 1
        # Right
        while b < len(row):
            if tree > int(row[b]):
                right_count += 1
            b += 1
        # Up
        while c >= 0:
            if tree > int(rows[c][i]):
                up_count += 1
            c -= 1
        # Down
        while d < len(rows):
            if tree > int(rows[d][i]):
                down_count += 1
            d += 1
        print(
            f"tree: {tree} -> up: {up_count}  right: {right_count} down: {down_count} left: {left_count}"
        )
