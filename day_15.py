def memory_game(start_numbers, max_turns):
    num_dict = {num: turn + 1 for turn, num in enumerate(start_numbers[:-1])}
    most_recent = start_numbers[-1]
    for turn in range(len(start_numbers), max_turns):
        if most_recent in num_dict:
            new_number = turn - num_dict[most_recent]
        else:
            new_number = 0
        num_dict[most_recent] = turn
        most_recent = new_number
    return most_recent


with open('input_day_15.txt', 'r') as f:
    start_numbers = f.read().splitlines()[0].split(',')

start_numbers  =[int(num) for num in start_numbers]

solution1 = memory_game(start_numbers, 2020)
solution2 = memory_game(start_numbers, 3 * 10**7)

print('A1: ', solution1)
print('A2: ', solution2)
