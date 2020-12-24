def applyMask(mask, input_value):
    input_value = bin(input_value).replace('b', '')
    input_value = '0' * (36 - len(input_value)) + input_value

    value = []
    for m, v in zip(mask, input_value):
        if m == 'X':
            value.append(v)
        else:
            value.append(m)
    return int(''.join(value), 2)

def applyMask2(mask, input_address):
        address = []
        for element, adr in zip(mask, input_address):
            if element == 'X':
                address.append('X')
            elif element == '0':
                address.append(adr)
            elif element == '1':
                address.append(element)
        return ''.join(address)

def task1(lines):
    mask = None
    mem = {}

    for line in lines:
        if line[:4] == 'mask':
            mask = line.split(' ')[-1]
        else:
            address = int(line[line.index('[')+1:line.index(']')])
            value = int(line.split(' ')[-1])
            mem[address] = applyMask(mask, value)
    return sum([mem[key] for key in mem])

# own function instead of itertools.product to avoid imports
# function found on https://docs.python.org/3/library/itertools.html
def cartesian(alist, repeat):
    pools = [tuple(pool) for pool in alist] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def task2(lines):
    mask = None
    number_X = None
    mem = {}

    for line in lines:
        if line[:4] == 'mask':
            mask = line.split(' ')[-1]
            number_X = mask.count('X')
        else:
            address = int(line[line.index('[')+1:line.index(']')])
            value = int(line.split(' ')[-1])
            addr = bin(address).replace('b', '')
            addr = '0' * (36 - len(addr)) + addr
            address = applyMask2(mask, addr)
            sets = list(cartesian([[0, 1]], number_X))
            addresses = []
            for s in sets:
                a = address
                for k in range(1, number_X + 1):
                    a = a.replace('X', str(s[k-1]), 1)
                addresses.append(a)

            for ad in addresses:
                mem[int(ad, 2)] = value

    return sum([mem[key] for key in mem])


with open('input_day_14.txt', 'r') as f:
    lines = f.read().splitlines()

solution1 = task1(lines)
solution2 = task2(lines)

print('A1: ', solution1)
print('A2: ', solution2)
