from day11 import (
    get_abs_distans, 
    get_index_of_empty_rows, 
    get_index_of_empty_columns, 
    get_galaxy_cordinates,
    calculate_distans
    )
import pytest


field = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""



field_expanded = """
....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#......."""


def test_get_index_of_empty_rows():
    index_of_empty_rows = get_index_of_empty_rows(field)
    expected_rows = [3, 7]
    assert index_of_empty_rows.sort() == expected_rows.sort()
    
    
def test_get_index_of_empty_colums():
    index_of_empty_columns = get_index_of_empty_columns(field)
    expected_columns = [2, 5, 8]
    index_of_empty_columns.sort()
    assert index_of_empty_columns == expected_columns
        

def test_get_galaxy_cordinates():
    cordinates = get_galaxy_cordinates(field)
    expected = [(0, 3), 
            (1, 7),
            (2, 0),
            (4, 6),
            (5, 1),
            (6, 9),
            (8, 7),
            (9, 0),
            (9, 4)
            ]    
    
    assert cordinates == expected
    

def test_get_abs_distans():
    expanded_columns = [2, 5, 8]
    expanded_rows = [3, 7]
    expansion_rate = 1
    source_galaxy = (0, 3)
    target_galaxy = (1, 7)

    distans = get_abs_distans(
        source_galaxy, 
        target_galaxy, 
        expanded_rows, 
        expanded_columns, 
        expansion_rate
        )
    assert distans == 6
    
@pytest.mark.parametrize(
    "source,target,empty_spaces,expansion_rate,expected", 
    [
        (4, 7, [2, 5, 8], 2, 4), 
        (4, 7, [2, 5, 8], 3, 5),  
        (7, 4, [2, 5, 8], 2, 4), 
        ]
    )
def test_calculate_distans(
    source, 
    target, 
    empty_spaces, 
    expansion_rate,
    expected
    ):
    distans = calculate_distans(
        source=source, 
        target=target,
        empty_spaces=empty_spaces,
        expansion_rate=expansion_rate
        )
    assert distans == expected
    