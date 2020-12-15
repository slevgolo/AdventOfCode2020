def getRow(rows, line, place):
    if place == 7:
        return rows[0]
    else:
        if line[place] == 'F':
            rows = rows[:len(rows)//2]
        elif line[place] == 'B':
            rows = rows[len(rows)//2:]
        else:
            raise ValueError
        return getRow(rows, line, place+1)

def getColumn(columns, line, place):
    if place == 3:
        return columns[0]
    else:
        if line[place] == 'L':
            columns = columns[:len(columns)//2]
        elif line[place] == 'R':
            columns = columns[len(columns)//2:]
        else:
            raise ValueError
        return getColumn(columns, line, place+1)


with open('input_day_5.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]

solution1 = [getRow(
    list(range(128)), line[:7], 0) * 8 + getColumn(
        list(range(8)), line[7:], 0) for line in lines]

solution1.sort()
solution2 = [
    solution1[i] - 1 for i in range(len(solution1)) if (
        solution1[i] - solution1[i-1]) > 1][0]

print('A1: ', max(solution1))
print('A2: ', solution2)
