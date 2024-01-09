datastream_buffer = open("day6/in.txt").read().strip()
print(datastream_buffer)


# datastream_buffer = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

for i in range(4, len(datastream_buffer) - 1):
    if len(set(datastream_buffer[i-4:i])) == 4:
        print(i)
        break
