import logging


def read_file_str(input_file):
    file_object = open(input_file, 'r')
    return file_object.readlines()


def analyze_password(limits: str, character: str, password: str) -> bool:
    passwd = password.strip()

    list_of_limits = list(map(int, limits.split('-')))
    if (passwd[list_of_limits[0]-1] == character) ^ (passwd[list_of_limits[1]-1] == character):
        return True
    else:
        return False


def main():
    password_database = read_file_str("password_database.txt")
    nr_of_correct_passwords = 0
    for password_and_rule in password_database:
        list_of_password_and_rule = password_and_rule.split(':')
        password = list_of_password_and_rule[1]
        list_of_rule = list_of_password_and_rule[0].split(' ')
        limits = list_of_rule[0]
        character = list_of_rule[1]

        nr_of_correct_passwords += 1 if analyze_password(limits, character, password) else 0
    print(nr_of_correct_passwords)


if __name__ == '__main__':
    main()
