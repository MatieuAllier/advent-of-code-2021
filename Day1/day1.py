with open("inputs\day1.txt") as file:
    data = [int(line) for line in file]

# Part 1

counter = 0
for i in range(1, len(data)):
    counter += (data[i] > data[i-1])
print(counter)

# Part 2

sliding_window_data =[(data[i] + data[i+1] + data[i+2]) for i in range(len(data)-2)]
counter = 0
for i in range(1, len(sliding_window_data)):
    counter += (sliding_window_data[i] > sliding_window_data[i-1])
print(counter)