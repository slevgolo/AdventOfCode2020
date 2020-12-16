def inBags(bag):
    bags = []
    for line in lines:
        (new_bag, content) = line.split(' bags contain ')
        if bag in content:
            bags.append(new_bag)
    return bags

def containsBags(bag):
    bags = []
    for line in lines:
        (new_bag, content) = line.split(' bags contain')
        if bag == new_bag:
            for contained_bags in content.split(','):
                if contained_bags[:3] == ' no':
                    return []

                number = int(contained_bags[1:].split(' ')[0])
                single_bag = contained_bags[1:].split(' ')[1] + ' ' + contained_bags[1:].split(' ')[2]
                bags.append([single_bag] * number)
            return [a for b in bags for a in b]


with open('input_day_7.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]

bag = 'shiny gold'
solution1 = dict()
solution1[bag] = set(inBags(bag))
for _ in range(len(lines)):
    keys = list(solution1.keys())
    for key in keys:
        for new_bag in solution1[key]:
            solution1[new_bag] = set(inBags(new_bag))

solution2 = dict()
solution2[bag] = containsBags(bag)
for _ in range(len(lines)):
    keys = list(solution2.keys())
    for key in keys:
        for new_bag in solution2[key]:
            solution2[new_bag] = containsBags(new_bag)

count = 0
bag_contains = solution2[bag]
for _ in range(len(lines)):
    new_bag_contains = []
    count += len(bag_contains)
    for key in bag_contains:
        if len(solution2[key]) > 0:
            new_bag_contains.append(solution2[key])
    bag_contains = [i for j in new_bag_contains for i in j]
    if len(bag_contains) == 0:
        break

print('A1: ', len(solution1) - 1)
print('A2: ', count)
