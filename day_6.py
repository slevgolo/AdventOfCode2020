with open('input_day_6.txt', 'r') as f:
    groups = f.read().split('\n\n')

groups[-1] = groups[-1][:-1]

solution1 = []
solution2 = []
for group in groups:
    number_persons = group.count('\n') + 1
    chars = group.replace('\n', '')
    set_chars = set(chars)
    solution1.append(len(set_chars))
    number_chars = sum(
        [chars.count(set_char) == number_persons for set_char in set_chars])
    solution2.append(number_chars)

print('A1: ', sum(solution1))
print('A2: ', sum(solution2))
