

def get_calibration_value(calibration_value: str) -> int:
    for char in calibration_value:
        if char.isdigit():
            recovered = char
            break

    for char in reversed(calibration_value):
        if char.isdigit():
            recovered = recovered + char
            break

    return int(recovered)

def find_text_calc() -> int:
    


def calc_answer(calibration_values: list) -> int:
    answer = 0
    for calibration_value in calibration_values:
        answer += get_calibration_value(calibration_value)
    return answer


def find_text(calibration_value: str, i: int) -> bool:

    for number in numbers:
        end = len(number)
        print(f"number: {number}")
        print(f"calibration_value[i: end]: {calibration_value[i: end]}")
        if number in calibration_value[i: end]:
            print(f"number: {number}")
            return True

    return False


def get_calibration_value_part_two(calibration_value: str) -> int:
    print(f"calibration_value: {calibration_value}")
    numbers = ["one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]

    length = len(calibration_value)
    for i in range(length):
        if calibration_value[i].isdigit():
            index_first_digit = calibration_value[i]
            break
        else:
            is_text_number(calibration_value, i)

    i = len(calibration_value) - 1
    while i >= 0:
        if calibration_value[i].isdigit():
            index_last_digit = i
            break
        i -= 1

    if index_first_digit == 0:
        print(f"index_first_digit: {index_first_digit}")
        answer = calibration_value[index_first_digit]
    else:
        for number in numbers:
            if number in calibration_value:
                print(f"number: {number}")
                index_first_digit = calibration_value.index(number)
                print(f"index_first_digit: {index_first_digit}")
                answer = str(numbers.index(number) + 1)
                break

    if index_last_digit == len(calibration_value) - 1:
        print(f"index_last_digit: {index_last_digit}")
        answer = answer + calibration_value[index_last_digit]
    else:
        for number in numbers:
            if number in calibration_value:
                print(f"number: {number}")
                index_last_digit = calibration_value.index(number)
                print(f"index_last_digit: {index_last_digit}")
                answer = answer + str(numbers.index(number) + 1)
                break

    print(answer)


if __name__ == "__main__":
    with open("day1_part1.txt") as f:
        calibration_values = f.readlines()

    answer = calc_answer(calibration_values)
    print(f"part 1: {answer}")
    print(f"part 2: {answer}")
