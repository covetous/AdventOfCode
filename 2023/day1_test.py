from day1 import (
    calc_answer,
    get_calibration_value,
    get_calibration_value_part_two,
    is_text_number
)

import pytest


@pytest.mark.parametrize("test_value, expected_value",
                         [["pqr3stu8vwx", 38],
                          ["1abc2", 12],
                          ["a1b2c3d4e5f", 15],
                          ["treb7uchet", 77]]
                         )
def test_part1(test_value, expected_value):
    value = get_calibration_value(test_value)
    assert value == expected_value
    assert type(value) is int


def test_calc_answer():
    test_values = ["pqr3stu8vwx", "1abc2", "a1b2c3d4e5f", "treb7uchet"]
    expected_value = 142
    value = calc_answer(test_values)
    assert value == expected_value


@pytest.mark.parametrize("test_value, expected_value", [
    ["two1nine", 29],
    ["eightwothree", 83],
    ["abcone2threexyz", 13],
    ["xtwone3four", 24],
    ["4nineeightseven2", 42],
    ["zoneight234", 14],
    ["7pqrstsixteen", 76],
])
def test_find_digits(test_value, expected_value):
    answer = get_calibration_value_part_two(test_value)
    assert answer == expected_value


def test_is_text_number():
    test_value = "one"
    expected_value = True
    value = is_text_number(test_value, 0)
    assert value == expected_value
