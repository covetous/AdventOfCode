def read_file(target_file):
    file_object = open(target_file, 'r')
    return list(file_object.readlines())


def navigate_sub():
    navigation_data = read_file('input.txt')
    forward = 0
    depth = 0
    for instruction_data in navigation_data:
        intstruction = instruction_data.split()
        if intstruction[0] == 'forward':
            forward += int(intstruction[1])
        elif intstruction[0] == 'down':
            depth += int(intstruction[1])
        elif intstruction[0] == 'up':
            depth -= int(intstruction[1])
    print(f'Sum of depth {depth} and lenght {forward} is {depth*forward}')


if __name__ == '__main__':
    navigate_sub()