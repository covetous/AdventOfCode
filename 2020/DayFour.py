MANDATORY_FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    # 'cid'
]


def read_file(expense_file):
    file_object = open(expense_file, 'r')
    return file_object.readlines()


def split_into_passports(pass_file):
    passports = []
    passport = {}
    blank_lines = 0
    for line in pass_file:
        print(f'Line from file: {line}')
        if not line.strip():
            print(f'New passport: {passport}')
            passports.append(passport)
            passport = {}
            blank_lines += 1
        else:
            line.strip()
            fields = line.split(' ')
            for field in fields:
                values = field.split(':')
                passport.update({values[0].strip(): values[1].strip()})

    print(f'New passport: {passport}')
    passports.append(passport)
    blank_lines += 1

    print(f'Found {len(passports)} passports')
    print(f'Found {blank_lines} blank lines')
    return passports


def verify_passports(passports):
    is_valid = 0
    not_valid = 0
    for passport in passports:
        is_ok = True
        for field in MANDATORY_FIELDS:
            if passport.get(field) is None:
                print(f'Passport NOT valid {passport}')
                not_valid += 1
                is_ok = False
        if is_ok:
            print(f'Passport valid {passport}')
            is_valid += 1
    print(f'{not_valid} Not valid passports ')
    return is_valid


def main(file="passport_database.txt"):
    pass_file = read_file(file)
    passports = split_into_passports(pass_file)
    result = verify_passports(passports)
    print(f'Correct passports: {result}')


if __name__ == '__main__':
    main()
