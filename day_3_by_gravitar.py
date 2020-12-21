# https://www.youtube.com/watch?v=52BB-F7_0sk

import time

def read_puzzel(file):
    with open(file) as f:
        return [row.strip() for row in f]

def solve_puzzel_1(puzzel, x, y):
    px = py = 0
    max_x, max_y = len(puzzel[0]), len(puzzel)
    counter = 0
    while True:
        px, py = px+x, py+y
        if py >= max_y: return counter
        if puzzel[py][px % max_x] =='#': counter +=1
    
def solve_puzzel_2(puzzel):
    result = 1
    for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= solve_puzzel_1(puzzel, x, y)
    return result

def MasterB(puzzel): # puzzel 1
    index = 0 
    counter = 0 
    for slope in puzzel[1:]: 
        index += 3 
        if index >= len(slope): 
            index -= len(slope) 
        if slope[index] == "#": 
            counter += 1 
    return counter

puzzel = read_puzzel('day_3.txt')

start = time.perf_counter()
print('solution puzzel one:', solve_puzzel_1(puzzel, 3, 1),'solved in',  time.perf_counter()-start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', solve_puzzel_2(puzzel),'solved in',  time.perf_counter()-start, 'sec')

start = time.perf_counter()
print('solution MasterB:', MasterB(puzzel),'solved in',  time.perf_counter()-start, 'sec')
