def read_file(expense_file):
    file_object = open(expense_file, 'r')
    return file_object.readlines()


def split_into_passports(pass_file):
    passports = []
    i=0
    while i < len(pass_file):
        if len(pass_file[i]) == 0:
            passports.append(passport)

        i += 1


def main(file = "passport_database.txt"):
    pass_file = read_file(file)
    passports = []
    passports = split_into_passports(pass_file)


if __name__ == '__main__':
    main()