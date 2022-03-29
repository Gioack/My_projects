def arithmetic_arranger(problems):
    for each_operation in problems:
        each_operation = each_operation.replace("+","")
        each_operation = each_operation.replace("-","")
        each_operation = each_operation.replace(" ","")
        if each_operation == "":
            print("You can insert only digits")
            quit()
        for each_letter in each_operation:
            if not each_letter.isdigit():
                print("You can insert only digits")
                quit()
# The upper code explict that the input can only be composed of digits and ""
# and at the most one "+" or  "-" for each operation
    allthefirstpart = ''
    allthesecondpart = ''
    Dashes = ''
    for each_operation in problems:                          #123 + 49
        where_plus = each_operation.find('+')
        where_minus = each_operation.find('-')
        Where_plus_or_minus = max(each_operation.find('+'), each_operation.find('-')) #
        each_operation_part1 = each_operation[:Where_plus_or_minus].strip() #  33
        each_operation_part2 = each_operation[Where_plus_or_minus:]         #+ 332
#       TRYING SYSTEM SPACES AND OTHER
        each_operation_part1 = "  " + each_operation_part1
# BIG PROBLEM WHEN THERE IS 3 DIGITS UP AND 2 DIGITS DOWN
        if len(each_operation_part1) >= len(each_operation_part2):
            while len(each_operation_part1) > len(each_operation_part2):
                each_operation_part2 = each_operation_part2[:2] + " " + each_operation_part2[2:]
        if len(each_operation_part2) > len(each_operation_part1):
            while len(each_operation_part2) > len(each_operation_part1):
                each_operation_part1 = " " + each_operation_part1
        Sum = int(each_operation_part1.strip()) + int(each_operation_part2[2:].strip())
        if (allthefirstpart == ""):
            allthefirstpart = each_operation_part1
            allthesecondpart = each_operation_part2
            for digit in range(len(each_operation_part1)):
                Dashes = Dashes + '-'
        else:
            allthefirstpart = allthefirstpart + "    " + each_operation_part1
            allthesecondpart = allthesecondpart + "    " + each_operation_part2
            Dashes = Dashes + '    '
            for digit in range(len(each_operation_part1)):
                Dashes = Dashes + '-'
    all = allthefirstpart + '\n'+ allthesecondpart + '\n'+ Dashes
    return all
# Build a for loop and inside a while that is able to make each item on the same lenght.
# Resplit strings.
# arithmetic_arranger(input('Insert the numbers: '))

print(arithmetic_arranger(["3 + 6", "33 - 2", "4 + 433", "1 + 4933", "33 + 6", "382 - 2", "4533 + 43", "123 + 49"]))
