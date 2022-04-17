def arithmetic_arranger(problems, Show_result = False):
    if Control_length(problems) == True:
        return "Error: Too many problems."
    if Control_Operator(problems) == True:
        return "Error: Operator must be '+' or '-'."
    if Control_Existence_numbers(problems) == True:
        return "Error: Numbers must only contain digits."
    if Control_length_numbers(problems) == True:
        return "Error: Numbers cannot be more than four digits."
    allthefirstpart = ""
    allthesecondpart = ""
    Dashes = ""
    Results = ""
    all = ""
    for each_problem in problems:
        Where_plus_or_minus = max(each_problem.find('+'), each_problem.find('-'))
        each_problem_part1 = f'  {each_problem[:Where_plus_or_minus].strip()}'
        each_problem_part2 = f'{each_problem[Where_plus_or_minus]} {each_problem[Where_plus_or_minus + 1:].strip()}'
        # The code above looks like this and not simply like: each_problem_part2 = each_problem[Where_plus_or_minus:]
        # because of cases like "     3 +     3", it makes these situations completely fine
        if len(each_problem_part1) >= len(each_problem_part2):
            while len(each_problem_part1) > len(each_problem_part2):
                each_problem_part2 = f"{each_problem_part2[:2]} {each_problem_part2[2:]}"
        if len(each_problem_part2) > len(each_problem_part1):
            while len(each_problem_part2) > len(each_problem_part1):
                each_problem_part1 = f" {each_problem_part1}"
        if (allthefirstpart == ""):
            allthefirstpart = each_problem_part1
            allthesecondpart = each_problem_part2
            for digit in range(len(each_problem_part1)):
                Dashes += '-'
        else:
            allthefirstpart += f'    {each_problem_part1}'
            allthesecondpart += f'    {each_problem_part2}'
            Dashes += "    "
            for digit in range(len(each_problem_part1)):
                Dashes += '-'
        if Show_result == True:
            if '+' in each_problem:
                Result_of_2parts = str(int(each_problem_part1.strip()) + int(each_problem_part2[2:].strip()))
            else:
                Result_of_2parts = str(int(each_problem_part1.strip()) - int(each_problem_part2[2:].strip()))
            while len(Result_of_2parts) < len(each_problem_part1):
                Result_of_2parts = f" {Result_of_2parts}"
            if (Results == ""):
                Results = Result_of_2parts
            else:
                Results += f'    {Result_of_2parts}'
            all = f"\n{Results}"
    all = f"{allthefirstpart}\n{allthesecondpart}\n{Dashes}{all}"
    return all
def Control_length(problems):
    if len(problems) > 5:
        return True
def Control_Operator(problems):
    for each_problem in problems:
        if not (("+" in each_problem) or ("-" in each_problem)):
            return True
def Control_Existence_numbers(problems):
    for each_problem in problems:
        for each_digit in each_problem:
            if not ((each_digit.isdigit() == True) or (each_digit == "+") or (each_digit == "-") or (each_digit == " ")):
                return True
def Control_length_numbers(problems):
    for each_problem in problems:
        if "+" in each_problem:
            Numbers_as_a_list = each_problem.split("+")
        else:
            Numbers_as_a_list = each_problem.split("-")
        for number in Numbers_as_a_list:
            number = number.strip()
            if len(number) > 4:
                return True
print(arithmetic_arranger(["780 + 56", "3849 - 1784", "305 + 489"],True))
