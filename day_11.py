def adjacentOccupied(grid, i, j, len_row, len_col):
    if i == 0 and j == 0:
        occupied = [
            grid[i][j+1],
            grid[i+1][j],
            grid[i+1][j+1]
        ]
    elif i == len_col - 1 and j == len_row - 1:
        occupied = [
            grid[i-1][j-1],
            grid[i-1][j],
            grid[i][j-1]
        ]
    elif i == 0 and 0 < j < len_row - 1 :
        occupied = [
            grid[i][j-1],
            grid[i][j+1],
            grid[i+1][j-1],
            grid[i+1][j],
            grid[i+1][j+1]      
            ]
    elif j == 0 and 0 < i < len_col - 1 :
        occupied = [
            grid[i-1][j],
            grid[i-1][j+1],
            grid[i][j+1],
            grid[i+1][j],
            grid[i+1][j+1]
        ]
    elif i == 0 and j == len_row -1:
        occupied = [
            grid[i][j-1],
            grid[i+1][j-1],
            grid[i+1][j]
        ]
    elif i == len_col - 1 and j == 0:
        occupied = [
            grid[i][j+1],
            grid[i-1][j],
            grid[i-1][j+1]
        ]

    elif i == len_col - 1 and 0 < j < len_row - 1:
        occupied = [
            grid[i-1][j],
            grid[i-1][j+1],
            grid[i][j+1],
            grid[i][j-1],
            grid[i-1][j-1]
        ]
    elif 0 < i < len_col - 1 and j == len_row - 1:
        occupied = [
            grid[i-1][j],
            grid[i-1][j-1],
            grid[i][j-1],
            grid[i+1][j],
            grid[i+1][j-1]
        ]
    elif 0 < i < len_col - 1 and 0 < j < len_row - 1:
        occupied = [
            grid[i-1][j-1],
            grid[i][j-1],
            grid[i+1][j-1],
            grid[i-1][j],
            grid[i+1][j],
            grid[i-1][j+1],
            grid[i][j+1],
            grid[i+1][j+1]
        ]
    else:
        raise ValueError
    return occupied.count('#')

def adjacentOccupied2(grid, i, j, len_row, len_col):
    row = grid[i]
    r = row[:j]
    r.reverse()    

    col = [field[j] for field in grid]
    c = col[:i]
    c.reverse()

    occupied = [
        # right
        checkSeeable(row[j+1:]),
        # left
        checkSeeable(r), 
        # down
        checkSeeable(col[i+1:]),
        # top
        checkSeeable(c),
        # down right
        checkSeeable([grid[ii][jj] for ii, jj in zip(
            range(i+1, len_col), range(j+1, len_row))]),
        #  top left
        checkSeeable([grid[ii][jj] for ii, jj in zip(
            range(i-1, -1, -1), range(j-1 ,-1, -1))]),
        # top right
        checkSeeable([grid[ii][jj] for ii, jj in zip(
            range(i-1, -1, -1), range(j+1, len_row))]),
        # down left
        checkSeeable([grid[ii][jj] for ii, jj in zip(
            range(i+1, len_col), range(j-1, -1, -1))])
        ]

    return sum(occupied)

def checkSeeable(seats):
    if '#' in seats:
        if 'L' in seats:
            if seats.index('#') < seats.index('L'):
                return True
        else:
            return True
    return False

def fillSeats(grid, func):
    new_grid = [row.copy() for row in grid]
    changed = False
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == 'L':
                if func(grid, i, j, len(row), len(grid)) == 0:
                    changed = True
                    new_grid[i][j] = '#'
    return (changed, [row.copy() for row in new_grid])

def clearSeats(grid, func, limit):
    new_grid = [row.copy() for row in grid]
    changed = False
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            if grid[i][j] == '#':
                if func(grid, i, j, len(row), len(grid)) >= limit:
                    changed = True
                    new_grid[i][j] =  'L'
    return (changed, [row.copy() for row in new_grid])

def task(grid, func, limit):
    changed = True
    while changed:
        (changed, new_grid) = fillSeats(grid, func)
        grid = [row.copy() for row in new_grid]
        (changed, new_grid) = clearSeats(grid, func, limit)
        grid = [row.copy() for row in new_grid]
        

    return [col for row in grid for col in row].count('#')


with open('input_day_11.txt', 'r') as f:
    lines = f.read().splitlines()
    
grid = [list(line) for line in lines]

solution1 = task(grid, adjacentOccupied, 4)
solution2 = task(grid, adjacentOccupied2, 5)

print('A1: ', solution1)
print('A2: ', solution2)
