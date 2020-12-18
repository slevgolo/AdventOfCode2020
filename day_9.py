def isSum(target_number, numbers):
    sums = [
        number1 + number2 for i, number1 in enumerate(
            numbers) for number2 in numbers[(i+1):]]
    return target_number in sums

def findSum(target_number, lines):
    numbers = [int(line) for line in lines]
    for set_size in range(2, len(numbers)):
        for first_number in range(len(numbers)):
            if first_number + set_size <= len(numbers):
                if sum(numbers[
                    first_number:first_number+set_size]) == target_number:
                    return max(numbers[
                        first_number:first_number+set_size]) + min(
                            numbers[first_number:first_number+set_size])

    return 'No solution found!'


with open('input_day_9.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]

for i, line in enumerate(lines):
    if i > 24:
        numbers = [int(lines[k]) for k in range(i-25, i)]
        target_number = int(line)
        if not isSum(target_number, numbers):
            solution1 = line
            solution2 = findSum(target_number, lines)
            break

print('A1: ', solution1)
print('A2: ', solution2)
