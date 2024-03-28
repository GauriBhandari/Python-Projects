def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line1 = []
    line2 = []
    dash_line = []
    results = []

    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(operand1), len(operand2)) + 2
        line1.append(operand1.rjust(width))
        line2.append(operator + operand2.rjust(width - 1))
        dash_line.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2)).rjust(width)
            else:
                result = str(int(operand1) - int(operand2)).rjust(width)
            results.append(result)

    arranged_problems = [
        '    '.join(line1),
        '    '.join(line2),
        '    '.join(dash_line)
    ]

    if show_answers:
        arranged_problems.append('    '.join(results))

    return '\n'.join(arranged_problems)

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=False))
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
