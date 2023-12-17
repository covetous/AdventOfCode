import pandas


__input = "input_day11.txt"


def get_index_of_empty_rows(field: str):
    rows = field.split("\n")
    index_of_empty_rows = []
    i = 0
    for i in range(len(rows)):
        if '#' not in rows[i]:
            index_of_empty_rows.append(i)
        i = i + 1
    return index_of_empty_rows


def get_index_of_empty_columns(field: str):
    data_frame = pandas.DataFrame({"a": field.split()})
    data_frame = data_frame['a'].apply(lambda x: pandas.Series(list(x)))
    index_of_empty_columns = []
    for series_index, series_value in data_frame.items():
        if not series_value.str.contains('#').any():
            index_of_empty_columns.append(series_index)

    return index_of_empty_columns


def calculate_distans(
        source: int,
        target: int,
        empty_spaces: list[int],
        expansion_rate: int) -> int:
    if source > target:
        max = source
        min = target
    elif target > source:
        max = target
        min = source
    elif target == source:
        return 0
    expands = 0
    for space in empty_spaces:
        if space > min and space < max:
            expands = expands + 1

    distans = max - min
    distans = distans - expands + expands * expansion_rate
    return distans


def get_abs_distans(source_galaxy: tuple,
                    target_galaxy: tuple,
                    empty_spaces_row: list[int],
                    empty_spaces_column: list[int],
                    expansion_rate: int
                    ) -> int:

    row_distans = calculate_distans(source_galaxy[0], target_galaxy[0],
                                    empty_spaces=empty_spaces_row,
                                    expansion_rate=expansion_rate
                                    )
    column_distans = calculate_distans(source_galaxy[1], target_galaxy[1],
                                       empty_spaces=empty_spaces_column,
                                       expansion_rate=expansion_rate
                                       )

    return column_distans + row_distans


def get_galaxy_cordinates(field):
    galaxy_symbol = '#'
    x_rows = field.split()
    coordinates = []
    i = 0
    while i < len(x_rows):
        indexes = [pos for pos, char in enumerate(
            x_rows[i]) if char == galaxy_symbol]
        for index in indexes:
            coordinate = (i, index)
            coordinates.append(coordinate)
        i = i + 1
    return coordinates


def main(__input=__input):
    answer = 0

    with open(__input, 'r') as i:
        galaxy_map = i.read()

    coordinate = get_galaxy_cordinates(galaxy_map)
    empty_columns = get_index_of_empty_columns(galaxy_map)
    empty_rows = get_index_of_empty_rows(galaxy_map)
    expansion_rate = 1000000
    print(galaxy_map)
    print(f"coordinate: {coordinate}")
    print(f"empty_columns: {empty_columns}")
    print(f"empty_rows: {empty_rows}")

    number_of_coordinates = len(coordinate)
    co = coordinate.copy()
    co.pop(0)
    i = 0
    for i in range(number_of_coordinates):
        j = 0
        for j in range(len(co)):
            answer = answer + get_abs_distans(source_galaxy=coordinate[i],
                                              target_galaxy=co[j],
                                              empty_spaces_row=empty_rows,
                                              empty_spaces_column=empty_columns,
                                              expansion_rate=expansion_rate
                                              )
        if len(co) > 0:
            co.pop(0)

    print(f"Answer day 11 part 1: {answer}")
    return answer


if __name__ == "__main__":
    main()
