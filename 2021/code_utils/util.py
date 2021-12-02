def read_file(target_file):
    file_object = open(target_file, 'r')
    return list(map(int, file_object.readlines()))