def slope(line, y_pos, right, down):
    if line[y_pos//down * right % len(line)] == '#':
        return True
    else:
        return False
        
def product(array):
    if len(array) == 0:
        return 1
    else:
        return array[0] * product(array[1:])


with open('input_day_3.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]

solution1 = 0
solution2 = [0, 0, 0, 0, 0]
for y_pos, line in enumerate(lines):
    if y_pos >= 1:        
        if line[y_pos * 3 % (len(line))] == '#':
            solution1 += 1

        if slope(line, y_pos, 1, 1):
            solution2[0] += 1
        if slope(line, y_pos, 3, 1):
            solution2[1] += 1
        if slope(line, y_pos, 5, 1):
            solution2[2] += 1
        if slope(line, y_pos, 7, 1):
            solution2[3] += 1
        if y_pos % 2 == 0:
            if slope(line, y_pos, 1, 2):
                solution2[4] += 1

print('A1: ', solution1)
print('A2: ', product(solution2))
