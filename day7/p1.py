output = open("day7/test_in.txt").read().strip().splitlines()
# print(output)

current_dir = {}
stack = []

for line in output:
    if line[0] == "$":
        if line[2] == "c":
            directory = line[5:]
            if directory == "/":
                current_dir = {}
                stack = []
            elif directory == "..":
                current_dir = stack.pop()
            else:
                if directory not in current_dir:
                    current_dir[directory] = {}
                stack.append(current_dir)
                current_dir = current_dir[directory]

    else:
        dir_or_size, name = line.split()
        if dir_or_size == "dir":
            current_dir[name] = {}
        else:
            current_dir[name] = int(dir_or_size)

root = stack[0]
print(f"{root=}")


def solve(structure):
    if type(structure) == int:
        return structure, 0
    size = 0
    ans = 0
    for child in structure.values():
        s, a = solve(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return size, ans


print(solve(root)[0])
print(solve(root)[1])
