with open('input_day_13.txt', 'r') as f:
    plan = f.read().splitlines()

def chineseRemainder(bus_ids, offset, modulo):
    # see https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    x = 0
    for a, p in zip(offset, bus_ids):
        n = modulo // p
        inverse = pow(n, -1, p)
        x = (x + a * n * inverse) % modulo
    return x

init_timestamp = int(plan[0])
bus_ids = plan[1]
bus_ids1 = [int(bus_id) for bus_id in bus_ids.split(',') if bus_id.isdigit()]

bus_found = False
timestamp = init_timestamp
while not bus_found:
    for bus_id in bus_ids1:
        if timestamp % bus_id == 0:
            bus_found = True
            break
    timestamp += 1

solution1 = (timestamp - 1 - init_timestamp) * bus_id

bus_ids2 = [int(bus_id) for bus_id in bus_ids.split(',') if bus_id.isdigit()]
minutes_offset = [
    -i for i in range(
        len(bus_ids.split(','))) if bus_ids.split(',')[i].isdigit()]

modulo = 1
for bus in bus_ids2:
    modulo *= bus

solution2 = chineseRemainder(bus_ids2, minutes_offset, modulo)

print('A1: ', solution1)
print('A2: ', solution2)
