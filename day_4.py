import re


def fileToListOfDicts(txt):
    passports_txt = txt.replace('\n', ' ').split('  ')
    passports_txt[-1] = passports_txt[-1][:-1]

    passports = []
    for passport_txt in passports_txt:
        key_value_pairs = [p.split(':') for p in passport_txt.split(' ')]
        d = dict()
        for k in key_value_pairs:
            d.update({k[0]: k[1]})
        passports.append(d)
    return passports


def validKeys(dic):
    dickeys = list(dic.keys())
    dickeys.sort()
    keys1 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    keys1.sort()
    keys2 = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    keys2.sort()
    if dickeys == keys1 or dickeys == keys2:
        return True
    else:
        return False


def validNumber(unit, number):
    if unit == 'cm':
        if 150 <= number <= 193:
            return True
    if unit == 'in':
        if 59 <= number <= 76:
            return True
    return False


with open('input_day_4.txt', 'r') as f:
    txt = f.read()

passports_dict = fileToListOfDicts(txt)

counter_challenge_1 = 0
counter_challenge_2 = 0
for passport in passports_dict:
    if not validKeys(passport):
        continue
    else:
        counter_challenge_1 += 1

    if 1920 <= int(passport['byr']) <= 2002:
        if 2010 <= int(passport['iyr']) <= 2020:
            if 2020 <= int(passport['eyr']) <= 2030:
                if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    if len(passport['pid']) == 9 and passport['pid'].isdigit():
                        pattern = '[0-9,a-f]*'
                        if passport['hcl'][0] == '#' and re.match(pattern, passport['hcl'][1:]).span()[1] == 6 and len(passport['hcl']) == 7:
                            unit = passport['hgt'][-2:]
                            if unit in ['cm', 'in']:
                                number = int(passport['hgt'][:-2])
                                if validNumber(unit, number):
                                    counter_challenge_2 += 1

print('A1: ', counter_challenge_1)
print('A2: ', counter_challenge_2)
