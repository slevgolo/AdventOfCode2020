with open('input_day_1.txt', 'r') as f:
    txt = f.read().split('\n')[:-1]

numbers = [int(t) for t in txt]

solution1 = []
solution2 = []
for i, number1 in enumerate(numbers):
    for j, number2 in enumerate(numbers[i:]):
        if number1 + number2 == 2020:
            solution1.append(number1 * number2)
        for number3 in numbers[j:]:
            if number1 + number2 + number3 == 2020:
                solution2.append(number1 * number2 * number3)

print('A1: ', solution1)
print('A2: ', solution2)
