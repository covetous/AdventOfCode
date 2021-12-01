def read_file(target_file):
    file_object = open(target_file, 'r')
    return list(map(int, file_object.readlines()))

def main():

    input_data = read_file('input.txt')
    count = 0
    a = -1
    for line in input_data:
        if a != -1:
            if line > a:
                count += 1
        a = line
        print(f'depth: {a}')
    print(f'Larger than previous: {count}')

if __name__ == '__main__':
    main()