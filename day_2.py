with open('input_day_2.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]


solution1 = 0
solution2 = 0
for line in lines:
    min_amount = int(line.split('-')[0])
    max_amount = int(line.split('-')[1].split(' ')[0])
    char = line.split(':')[0][-1]
    password = line.split(':')[1][1:]
    if min_amount <= password.count(char) <= max_amount:
        solution1 += 1
    
    if password[min_amount-1] == char or password[max_amount-1] == char:
        if password[min_amount-1] != char or password[max_amount-1] != char:
            solution2 += 1

print('A1: ', solution1)
print('A2: ', solution2)
