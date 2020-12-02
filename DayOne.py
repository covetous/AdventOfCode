TARGET = 2020

def partOne(expense_file: str):
    file_object = open(expense_file, 'r')
    expense_report = list(map(int, file_object.readlines()))
    sums = []
    for expense in expense_report:
        if (2020-expense) in expense_report:
            sums.append(expense)

    result = 1
    for i in sums:
        result = i * result
    return result
    
def read_file(expense_file)
    file_object = open(expense_file, 'r')
    return list(map(int, file_object.readlines()))

def find_multipliers(expense_report, product, current_values, index):
    while index < len(expense_report):
        value = expense_report[index]
        if value + product = 2020:
             return value, True

        if product < target:
                return product, current_values
        index =+ 1

def starter(expense_report):
    while index =< len(expense_report) and len(expense_report[index]) == 0:
        find_multipliers()

def main():
    result = partOne('expense_report.txt')
    print(f'Result method 1: {result}')

    expense_report = read_file('expense_report.txt')
    product, sums = find_multipliers(expense_report)
    print(f'Result method 2 {product} with the values {sums}')


if __name__ == "__main__":
    main()
