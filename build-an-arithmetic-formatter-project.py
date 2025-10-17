** start of main.py **

import re

NOT_NUMBER_PATTERN = '[^0-9]'

def arithmetic_arranger(problems, show_answers=False):
    if invalid_problems:=problems_validator(problems):
        return invalid_problems
    operand1s = []
    operand2s = []
    dashes = []
    answers = []
    for problem in problems:
        parts = problem.split(' ')
        
        operand1, operator, operand2 = parts
        if invalid_operator:=operator_validator(operator):
            return invalid_operator
        if invalid_operand:=operand_validator(operand1, operand2):
            return invalid_operand
        max_length = max([len(operand1), len(operand2)])
        dash_length = max_length+2
        operand1s.append(f'{operand1:>{dash_length}}')
        operand2s.append(f'{operator} {operand2:>{max_length}}')
        dashes.append('-'*(max_length+2))
        if show_answers:
            op1 = int(operand1)
            op2 = int(operand2)
            if operator == '+':
                result = str(op1 + op2)
            else:
                result = str(op1 - op2)
            answers.append(f'{result:>{dash_length}}')

    output = '    '.join(operand1s)
    output += '\n' + '    '.join(operand2s)
    output += '\n' + '    '.join(dashes)
    if show_answers:
        output += '\n' + '    '.join(answers)
    return output
        
def problems_validator(problems):
    if len(problems) > 5:
        return 'Error: Too many problems.'

def operator_validator(operator):
    if operator not in ('+', '-'):
        return "Error: Operator must be '+' or '-'."
    return None

def operand_validator(operand1, operand2):
    if len(operand1) > 4 or len(operand2) > 4:
        return 'Error: Numbers cannot be more than four digits.'
    if (re.search(NOT_NUMBER_PATTERN, operand1)
        or re.search(NOT_NUMBER_PATTERN, operand2)
        ):
        return 'Error: Numbers must only contain digits.'

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')

** end of main.py **

