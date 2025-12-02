from aocd import data

# part 1
position = 50
count = 0

for line in data.split():
    direction = line[0]
    distance = int(line[1:len(line)])
    if direction == 'R':
        position = (position + distance) % 100
    if direction == 'L':
        position = (position - distance) % 100
    if position == 0:
        count = count + 1

print(count)

# part 2