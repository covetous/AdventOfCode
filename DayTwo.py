import logging


def read_file_str(input_file):
    logging.info(f'Reading file {input_file}')
    file_object = open(input_file, 'r')
    return file_object.readlines()


def analyze_password(occurence_limits: str, character: str, password: str) -> bool:
    counts = 0
    for c in password.strip():
        counts += 1 if c == character else 0
    
    list_of_limits = list(map(int, occurence_limits.split('-')))
    if list_of_limits[0] <= counts <= list_of_limits[1]:
        logging.info(f'Found a correct password. Pattern {list_of_limits} {character}: {password}')
        return True
    else:
        return False


def main():
    logging.info("Starting Advent of Code day 2")
    password_database = read_file_str("password_database.txt")
    nr_of_correct_passwords = 0
    logging.info(f'Going through {len(password_database)} lines of passwords.')
    for password_and_rule in password_database:
        list_of_password_and_rule = password_and_rule.split(':')
        password = list_of_password_and_rule[1]
        list_of_rule = list_of_password_and_rule[0].split(' ')
        limits = list_of_rule[0]
        character = list_of_rule[1]

        nr_of_correct_passwords += 1 if analyze_password(limits, character, password) else 0
    logging.info(f'Found {nr_of_correct_passwords} occurense of correct passwords.')
    print(nr_of_correct_passwords)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
