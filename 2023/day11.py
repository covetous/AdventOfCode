import pandas

def get_index_of_empty_rows(field: str):
    rows = field.split("\n")
    index_of_empty_rows = []
    for row in rows:
        if '#' not in row:
            index_of_empty_rows.append(rows.index(row))
            
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
    if source > target : max = source; min = target
    elif target > source : max = target; min = source
    elif target == source: return 0
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
                    expansion_rate:int
                    ) -> list:
    for space in empty_spaces_row:
        if source_galaxy[0] < space < target_galaxy[0]:
            expand = expand + 1
    distans = abs(source_galaxy[0] - target_galaxy[0])
    distans = distans + abs(source_galaxy[1] - target_galaxy[1])
    return distans

def get_galaxy_cordinates(field):
    galaxy_symbol = '#'
    x_rows = field.split()
    coordinates = []
    i=0
    while i < len(x_rows):
        indexes = [pos for pos, char in enumerate(x_rows[i]) if char == galaxy_symbol]
        for index in indexes:   
            coordinate = (i, index)
            print(f"coordinate: {coordinate}")
            coordinates.append(coordinate)
        i = i + 1
    print(f"coordinates: {coordinates}")
    return coordinates
        
        