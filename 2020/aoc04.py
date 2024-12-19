# --- Day 4: Passport Processing ---
import re

with open('input/aoc04_input.txt') as f:
    content = f.read().split('\n\n')
    passports = [re.split('[\n\s]', line) for line in content]
    pass_dict = [dict([(line.split(":")) for line in passport]) for passport in passports]

# -- Part1: Count passports that have all required fields. Treat cid as optional. --
def valid_length(passports):
    valids = []
    for passport in passports:
        if len(passport) >= 8:
            valids.append(passport)
        if len(passport) == 7:
            valids.append(passport)
            for item in passport:
                if 'cid' in item:
                    valids.remove(passport)
    print(f"Valid by length: {len(valids)}")
    return valids


# -- Part 2: Count passwords that have valid values. cid optional. --

# Rules for validity
byr = range(1920, 2002+1)
iyr = range(2010, 2020+1)
eyr = range(2020, 2030+1)
hgt = [str(cm)+'cm' for cm in range(150, 193+1)] + [str(inch)+'in' for inch in range(59, 76+1)]
hcl = int('ffffff', 16)
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


valid_len = valid_length(pass_dict)
valids = valid_len.copy()

for passport in valid_len:
    if int(passport['byr']) not in byr:
        # print(f"byr invalid: {passport['byr']}")
        valids.remove(passport)
    elif int(passport['iyr']) not in iyr:
        # print(f"iry invalid: {passport['iyr']}")
        valids.remove(passport)
    elif int(passport['eyr']) not in eyr:
        # print(f"eyr invalid: {passport['eyr']}")
        valids.remove(passport)
    elif passport['hgt'] not in hgt:
        print(f"hgt invalid: {passport['hgt']}")
        valids.remove(passport)
    elif passport['hcl'][0] != "#":
        print(f"hcl no #: {passport['hcl']}")
        valids.remove(passport)
    elif len(passport['hcl']) != 7:
        print(f"hcl {passport['hcl']} too short")
        valids.remove(passport)
    elif int(passport['hcl'].strip('#'), 16) >= hcl:
        print(f"hcl {passport['hcl'].strip('#')} out of bounds: {passport}")
        valids.remove(passport)
    elif passport['ecl'] not in ecl:
        print(f"ecl invalid: {passport['ecl']}")
        valids.remove(passport)
    elif len(passport['pid']) != 9:
        print(f"pid invalid: {passport['pid']}")
        valids.remove(passport)

print(f"Valid passwords: {len(valids)}")
