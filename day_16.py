import re


def isValid(rules_dict, number):
    valid = False
    for value in rules_dict.values():
        if (
            number in range(int(value[0]), int(value[1]) + 1)) or (
                number in range(int(value[2]), int(value[3])+1)):
                valid = True
                break
    return valid

def task2(rules_dict, nearby_tickets, known_keys, known_numbers):
    dic = {}
    for key, value in rules_dict.items():
        if not key in known_keys:
            for num in range(len(nearby_tickets[0].split(','))):
                if not num in known_numbers:
                    is_possible = []
                    for ticket in nearby_tickets:
                        number = int(ticket.split(',')[num])
                        valid = None
                        if (
                        number in range(int(value[0]), int(value[1]) + 1)) or (
                            number in range(int(value[2]), int(value[3])+1)):
                            valid = True
                        else:
                            valid = False
                        is_possible.append(valid)
                    if all(is_possible):
                        if num in dic.keys():
                            dic[num].append(key)
                        else:
                            dic[num] = [key]
    return dic


with open('input_day_16.txt', 'r') as f:
    inp = f.read().split('\n\n')
    rules = inp[0].splitlines()
    my_ticket = inp[1].splitlines()[-1]
    nearby_tickets = inp[2].splitlines()[1:]

rules_dict = {rule.split(':')[0]: re.findall(r'(\d+)', rule) for rule in rules}

invalid_numbers = []
invalid_ticket_ids = []
for ticket in nearby_tickets:
    numbers = ticket.split(',')
    for number in numbers:
        if not isValid(rules_dict, int(number)):
                invalid_numbers.append(int(number))
                invalid_ticket_ids.append(nearby_tickets.index(ticket))

solution1 = sum(invalid_numbers)

nearby_tickets = [
    nticket for t_id, nticket in enumerate(
        nearby_tickets) if not t_id in invalid_ticket_ids]

known_keys = []
known_numbers = []
res_dict = {}
for _ in range(20):
    d = task2(rules_dict, nearby_tickets, known_keys, known_numbers)
    for k, v in d.items():
        if len(v) == 1:
            known_keys.append(v[0])
            res_dict[v[0]] = k

solution2 = 1
for k, v in res_dict.items():
    if k[:9] == 'departure':
        solution2 *= int(my_ticket.split(',')[v])


print('A1: ', solution1)
print('A2: ', solution2)
