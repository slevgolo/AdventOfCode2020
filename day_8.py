def task1(lines):
    counter = 0
    infinit_loop = False
    i_out_of_bounds = False
    i = 0
    used_lines = []
    while not infinit_loop and not i_out_of_bounds:
        if i in used_lines:
            infinit_loop = True
        elif not (0 <= i <= len(lines) -1 ):
            i_out_of_bounds = True
        else:
            used_lines.append(i)
            line = lines[i]
            instruction= line.split(' ')[0]
            if instruction == 'acc':
                counter += int(line.split(' ')[1])
                i += 1
            elif instruction == 'nop':
                i += 1
            elif instruction == 'jmp':
                i += int(line.split(' ')[1])
            else:
                raise ValueError
    return (infinit_loop, i_out_of_bounds, counter)


with open('input_day_8.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]

_, _, solution1 = task1(lines)

for k in range(2):
    for i in range(len(lines)):
        original_line = lines[i]
        if k == 0:
            new_line = lines[i].replace('jmp', 'nop')
        if k == 1:
            new_line = lines[i].replace('nop', 'jmp')
        lines[i] = new_line
        infinit_loop, i_out_of_bounds, solution2 = task1(lines)
        if infinit_loop:
            lines[i] = original_line
        else:
            break
    if not infinit_loop:
        break


print('A1: ', solution1)
print('A2: ', solution2)
