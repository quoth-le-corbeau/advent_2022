output = open("day7/in.txt").read().strip().splitlines()
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


def total_size(root_directory: dict) -> int:
    total = 0
    for val in root_directory.values():
        if type(val) == int:
            total += val
        elif type(val) == dict:
            total += total_size(val)

    return total


print(total_size(root_directory=root))


def size(folder) -> int:
    if type(folder) == int:
        return folder
    else:
        return sum(map(size, folder.values()))


print(size(folder=root))


t = size(root) - 40_000_000


def solve(dir):
    ans = float("inf")
    if size(dir) >= t:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = solve(child)
        ans = min(ans, q)
    return ans


print(solve(root))
