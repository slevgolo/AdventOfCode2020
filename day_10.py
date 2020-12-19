def prod(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] * prod(numbers[1:]) 


with open('input_day_10.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]

lines = sorted([int(line) for line in lines])
lines = [0] + lines + [max(lines) + 3]
diffs = [lines[i+1] - lines[i] for i in range(len(lines) - 1)]
solution1 = diffs.count(1) * diffs.count(3)

# must contain
ids_contain = [i+1 for i in range(len(diffs)) if diffs[i] == 3]
ids_contain += [i-1 for i in ids_contain] + [0]
ids_contain = sorted(list(set(ids_contain)))

# exponents to determine nubmer of subsets
id_diffs = [
    ids_contain[i+1] - ids_contain[i] - 1 for i in range(len(ids_contain) - 1)]

# if diff of ids is 3, empty set is not a valid subset!
numbers_subsets = [2**k for k in id_diffs if 0 < k < 3]
numbers_subsets += [2**k - 1 for k in id_diffs if k == 3]

solution2 = prod(numbers_subsets)
print('A1: ', solution1)
print('A2: ', solution2)
