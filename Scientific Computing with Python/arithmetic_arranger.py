#######################################################################################################
#                                                                                                     #
#                                         Arithmetic Arranger                                         #
#                                                                                                     #
#      Takes input list of addition and/or subtraction expressions (e.g. ["12 + 34", "567 - 890"])    # 
#      and converts each expression to vertical format (see below) with the option of including       #
#      the answer.                                                                                    #
#                                                                                                     #
#      Example of vertical format:                                                                    #
#                                                                                                     #
#                   12      567                                                                       #
#                 + 34    - 890                                                                       #
#                 ----    -----                                                                       #
#                   46     -323                                                                       #
#                                                                                                     #
#######################################################################################################

def error_handler(problems):

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:

        if problem[1] != '+' and problem[1] != '-':
            return "Error: Operator must be '+' or '-'."

        if not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."

        problem_width = max(len(problem[0]), len(problem[2]))

        if problem_width > 4:
            return "Error: Numbers cannot be more than four digits."

    return None


def calculate_answer(split_problem):

    if split_problem[1] == '+':
        return int(split_problem[0]) + int(split_problem[2])

    else:
        return int(split_problem[0]) - int(split_problem[2])


def problem_formatter(problem_dicts):

    spacing = ' ' * 4

    problem_strings = [

        spacing.join([
            ('{:>' + str(problem_dict['width']) + '}').format(problem_dict['first_operand'])
            for problem_dict in problem_dicts
        ]),

        spacing.join([
            ('{}' + '{:>' + str(problem_dict['width'] - 1) + '}').format(problem_dict['operator'], problem_dict['second_operand'])
            for problem_dict in problem_dicts
        ]),

        spacing.join([
            '-' * problem_dict['width']
            for problem_dict in problem_dicts
        ]),

        spacing.join([
            ('{:>' + str(problem_dict['width']) + '}').format(problem_dict['answer'])
            for problem_dict in problem_dicts
            if problem_dict['answer'] is not None
        ])

    ]

    if problem_strings[3] == '':
        problem_strings.pop(3)

    return '\n'.join(problem_strings)


def arithmetic_arranger(problems, show_answers=False):

    expanded_problems = [
        problem.split() 
        for problem in problems
    ]  

    if error_handler(expanded_problems) is not None:
        return error_handler(expanded_problems)

    answers = [
        calculate_answer(problem) if show_answers
        else None
        for problem in expanded_problems
    ]

    problem_components = [
        {
            'first_operand': problem[0],
            'second_operand': problem[2],
            'operator': problem[1],
            'answer': answers[expanded_problems.index(problem)],
            'width': max(len(str(problem[0])), len(str(problem[2]))) + 2
        } 
        for problem in expanded_problems
    ]

    arranged_problems = problem_formatter(problem_components)

    return arranged_problems


print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
