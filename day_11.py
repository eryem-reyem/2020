import time

def get_puzzel_list(file):
    with open(file) as f:
        return [row.strip() for row in f]
puzzel = get_puzzel_list('day_11.txt')

def solve_puzzel_1(puzzel):
    new_puzzel = puzzel[:]

    def count_adjacent(x, y, puzzel):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        adjacent = ''
        for dx, dy in directions:
            if 0 <= x+dx < len(puzzel[0]) and 0 <= y+dy < len(puzzel):
                adjacent = adjacent + puzzel[y+dy][x+dx]
        return adjacent

    while True:
        count = 0
        temp_puzzel = []
        for y in range(len(new_puzzel)):
            temp_string = ''
            for x in range(len(new_puzzel[y])):
                if new_puzzel[y][x] == '.':
                    temp_string = temp_string + new_puzzel[y][x]
                    continue
                adjacent = count_adjacent(x, y, new_puzzel)
                if adjacent.count('#') >= 4:
                    temp_string = temp_string + 'L'
                elif adjacent.count('#') == 0:
                    temp_string = temp_string + '#'
                else:
                    temp_string = temp_string + new_puzzel[y][x]
            temp_puzzel.append(temp_string)
        if temp_puzzel == new_puzzel:
            for i in temp_puzzel:
                count = count + i.count('#')
            return count
        else:
            new_puzzel = temp_puzzel[:]
        
def solve_puzzel_2(puzzel):
    new_puzzel = puzzel[:]

    def count_adjacent(x, y, puzzel):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        adjacent = ''
        for dx, dy in directions:
            check_x, check_y = x+dx, y+dy 
            while True:
                if 0 <= check_x < len(puzzel[0]) and 0 <= check_y < len(puzzel):
                    if puzzel[check_y][check_x] != '.':
                        adjacent = adjacent + puzzel[check_y][check_x]
                        break
                    else:
                        check_x += dx
                        check_y += dy
                else:
                    break

        return adjacent

    while True:
        count = 0
        temp_puzzel = []
        for y in range(len(new_puzzel)):
            temp_string = ''
            for x in range(len(new_puzzel[y])):
                if new_puzzel[y][x] == '.':
                    temp_string = temp_string + new_puzzel[y][x]
                    continue
                adjacent = count_adjacent(x, y, new_puzzel)
                if adjacent.count('#') >= 5:
                    temp_string = temp_string + 'L'
                elif adjacent.count('#') == 0:
                    temp_string = temp_string + '#'
                else:
                    temp_string = temp_string + new_puzzel[y][x]
            temp_puzzel.append(temp_string)
        if temp_puzzel == new_puzzel:
            for i in temp_puzzel:
                count = count + i.count('#')
            return count
        else:
            new_puzzel = temp_puzzel[:]

start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(puzzel), 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel_2(puzzel), 'solved in', time.perf_counter() - start, 'sec')