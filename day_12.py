def manhattenDistance(position):
    return abs(position[0]) + abs(position[1]) 

def move(direction, value, position):
    if direction == 'N':
        position = [position[0], position[1] + value]
    elif direction == 'E':
        position = [position[0] + value, position[1]]
    elif direction == 'S':
        position = [position[0], position[1] - value]
    elif direction == 'W':
        position = [position[0] - value, position[1]]
    else:
        raise ValueError
    return position

with open('input_day_12.txt', 'r') as f:
    instructions = f.read().splitlines()

start_facing = 'E'
start_position = [0, 0]

facings = ['N', 'E', 'S', 'W']
position = start_position
facing = start_facing
for instruction in instructions:
    command = instruction[0]
    value = int(instruction[1:])

    if command == 'F':
        position = move(facing, value, position)
    elif command == 'R':
        facing = facings[(facings.index(facing) + value // 90) % 4]
    elif command == 'L':
        facing = facings[(facings.index(facing) - value // 90) % 4]
    elif command in facings:
        position = move(command, value, position)

solution1 = manhattenDistance(position)
print('A1: ', solution1)

waypoint = [10, 1]
position = start_position
facing = start_facing
for instruction in instructions:
    command = instruction[0]
    value = int(instruction[1:])

    if command == 'F':
        position = [
            position[0] + value * waypoint[0],
            position[1] + value * waypoint[1]
            ]
    elif command in facings:
        waypoint = move(command, value, waypoint)
    elif command in ['R', 'L'] and value == 180:
        waypoint = [-waypoint[0], -waypoint[1]]
    elif command == 'L' and value in [90, 270]:
        if value // 90 == 1:
            waypoint = [-waypoint[1], waypoint[0]]
        elif value // 90 == 3:
            waypoint = [waypoint[1], -waypoint[0]]
    elif command == 'R' and value in [90, 270]:
        if value // 90 == 1:
            waypoint = [waypoint[1], -waypoint[0]]
        elif value // 3:
            waypoint = [-waypoint[1], waypoint[0]]

solution2 = manhattenDistance(position)
print('A2: ', solution2)
