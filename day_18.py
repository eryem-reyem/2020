import time   

def get_puzzel_list(file):
    with open(file) as f:
        return [row.strip().replace(' ', '') for row in f]


def calc(number_1, number_2, operator):
    if operator == '+':
        return number_1 + number_2
    else:
        return number_1 * number_2


def priorität(op, part):
    if part == 'puzzel_1':
        if op in '+*': return 1
        else: return 0
    else:
        if op == '+': return 2
        elif op == '*': return 1
        else: return 0


def solve_puzzel(puzzel, part):
    result = 0

    for line in puzzel:
        numbers = []
        ops = []

        for char in line:

            if char not in '+*()':
                numbers.append(int(char))    
            elif char == '(':
                ops.append(char)
            elif char == ')':
                while ops[-1] != '(':
                    numbers.append(calc(numbers.pop(), numbers.pop(), ops.pop()))
                ops.pop()
            else:
                while ops and priorität(ops[-1], part) >= priorität(char, part):
                    numbers.append(calc(numbers.pop(), numbers.pop(), ops.pop()))
                ops.append(char)

        while ops:
            numbers.append(calc(numbers.pop(), numbers.pop(), ops.pop()))

        result += numbers[0]

    return result


puzzel = get_puzzel_list('day_18.txt')

start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel(puzzel, 'puzzel_1'), 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel(puzzel, 'puzzel_2'), 'solved in', time.perf_counter() - start, 'sec')