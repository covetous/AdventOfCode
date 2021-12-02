def read_file(target_file):
    file_object = open(target_file, 'r')
    return list(file_object.readlines())


def navigate_sub():
    navigation_data = read_file('input.txt')
    forward = 0
    depth = 0
    aim = 0
    for instruction_data in navigation_data:
        intstruction = instruction_data.split()
        if intstruction[0] == 'forward':
            forward += int(intstruction[1])
            print(f'Increased forward with {intstruction[1]} to {forward}')
            depth = depth + aim * int(intstruction[1])
            print(f'Increased depth with {int(intstruction[1])} times aim {aim} to {depth}')
        elif intstruction[0] == 'down':
            aim += int(intstruction[1])
            print(f'Increased aim with {int(intstruction[1])} to {aim}')
        elif intstruction[0] == 'up':
            aim -= int(intstruction[1])
            print(f'Reduced aim with {int(intstruction[1])} to {aim}')
    print(f'Sum of depth {depth} and lenght {forward} is {depth*forward}')


if __name__ == '__main__':
    navigate_sub()