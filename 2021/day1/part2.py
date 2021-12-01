def read_file(target_file):
    file_object = open(target_file, 'r')
    return list(map(int, file_object.readlines()))

def main():
    depths = read_file('input.txt')
    count = 0
    aggregated_depths = list()
    for i in range(len(depths)):
        if len(depths)-i > 2:
            d = depths[i] + depths[i+1] + (depths[i+2])
            aggregated_depths.append(d)

    a = -1
    for depth in aggregated_depths:
        if a != -1:
            if depth > a:
                count += 1
        a = depth

    print(f'Larger than previous: {count}')

if __name__ == '__main__':
    main()