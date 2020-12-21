import time

def get_puzzel_list(file):
    with open(file) as f:
        return [int(row.strip()) for row in f]

puzzel = sorted(get_puzzel_list('day_10.txt'))
puzzel.insert(0, 0)
puzzel.append(max(puzzel) + 3)

def solve_puzzel_1(puzzel):
    one = two = three = 0

    for i in range(len(puzzel)):
        if i+1 < len(puzzel) :
            number = puzzel[i+1] - puzzel[i]
        else:
            break
        
        if number == 1:
            one += 1
        elif number == 2:
            two += 1
        elif number == 3:
            three += 1

    return ((one) * (three))

def count_paths(puzzel):  # by: https://www.youtube.com/watch?v=lXqOS6_yYJo&t=63s
    output = puzzel[-1]
    
    # num_ways[i] is the numbers of ways to get to i
    num_ways = [0] * (output + 1)
    
    if 1 in puzzel:
        num_ways[1] = 1
        

    if 2 in puzzel and 1 in puzzel:
        num_ways[2] = 2    
    elif 2 in puzzel:
        num_ways[2] = 1
        

    for n in range(3, output + 1):
        if n not in puzzel:
            continue
        num_ways[n] = num_ways[n-3] + num_ways[n-2] + num_ways[n-1]

    return num_ways[output]

def löse(puzzel):           # by https://www.youtube.com/watch?v=FqJ_EwbXAPE
    diffs = ''.join([str(b-a) for a, b in zip(puzzel, puzzel[1:])])
    part_1 = diffs.count('1') * diffs.count('3')

    diffs = diffs.replace('1111', 'a').replace('111', 'b').replace('11', 'c')
    part_2 = 7**diffs.count('a') * 4**diffs.count('b') * 2**diffs.count('c')

    return part_1, part_2

def morpheus(puzzel):       # https://www.youtube.com/watch?v=4HFHUJmEUxg
    poss = [1] + [0] * puzzel[-1]
    for i in puzzel[1:]:
        poss[i] = poss[i-1] + poss[i-2] + poss[i-3]
    return poss[-1]

start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(puzzel), 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', count_paths(puzzel),  ' solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel one and two:', '\t', löse(puzzel),  ' solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', morpheus(puzzel),  ' solved in', time.perf_counter() - start, 'sec')