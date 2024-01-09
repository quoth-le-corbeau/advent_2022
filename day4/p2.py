groups = open("day4/in.txt").read().strip().split("\n")
count = 0
for group in groups:
    markers = group.replace("-", ",").split(",")
    group_1_touch_2 = int(markers[2]) <= int(markers[0]) <= int(markers[3]) or int(markers[2]) <= int(markers[1]) <= int(markers[3])
    group_2_touch_1 = int(markers[0]) <= int(markers[2]) <= int(markers[1]) or int(markers[0]) <= int(markers[3]) <= int(markers[1])
    if group_1_touch_2 or group_2_touch_1:
        count += 1


print(count)
