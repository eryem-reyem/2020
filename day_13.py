import time

def get_puzzel_list(file):
    with open(file) as f:
        return [row.strip().split(',') for row in f]
get_input = get_puzzel_list('day_13.txt')


def solve_puzzel_1(get_input):
    puzzel = []
    for y in range(len(get_input)):
        puzzel.append([])
        for x in get_input[y]:
            if x == 'x': continue
            else: puzzel[y].append(int(x))
        puzzel[y] = sorted(puzzel[y])
    times = {}
    for number in puzzel[1]:
        times[number] = (((puzzel[0][0] // number) * number) + number) - puzzel[0][0]
    return min(times.values()) * list(times.keys())[list(times.values()).index(min(times.values()))]



start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(get_input), 'solved in', time.perf_counter() - start, 'sec')