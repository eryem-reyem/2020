import time                   
from collections import defaultdict
import math

def read_puzzle(file):
  with open(file) as f:
    return f.read().split('\n\n')


def get_borders(puzzel):
    borders = {}

    for tile in puzzel:
        temp_list = tile.split('\n')
        reference = int
        top, bottum, left, right = [], [], [], []
        
        for count, line in enumerate(temp_list):
            if 'Tile' in line:
                reference = int(line[5:-1])
            else:
                left.append(line[0])
                right.append(line[len(line)-1])

            if count == 1:
                top.append(line)
            elif count == len(line):
                bottum.append(line)

        left = [''.join(left)]
        right = [''.join(right)]
        border = [top[0], bottum[0], left[0], right[0], top[0][::-1], bottum[0][::-1], left[0][::-1], right[0][::-1]]

        for i in border:
            if i in borders.keys():
                value = borders[i]
                value.append(reference)
                #print(i, value)
                borders[i] = value
            else:
                borders[i] = [reference]

    return borders


def solve_puzzel_1(puzzel):
    borders = get_borders(puzzel)
    adjacents = defaultdict(set)
    result = 1

    for value in borders.values():
        if len(value) == 1:
            continue
        
        value_1 = value[0]
        value_2 = value[1]
        
        adjacents[value_1].add(value_2)
        adjacents[value_2].add(value_1)

    for i in adjacents:
        if len(adjacents[i]) == 2:
            result *= i
    
    return result


def solve_puzzel_2(puzzel):
    big_puzzel = []
    temp_puzzel = []
    RAW = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
    sea_monster = RAW.split('\n')
    coordinates = []
    #print(math.sqrt(len(puzzel)))

    for i in range(int(math.sqrt(len(puzzel)))):
        temp_puzzel.append([])

    for count, tile in enumerate(puzzel):
        #print(count%int(math.sqrt(len(puzzel))))
        temp_tile = tile.split('\n')

        for row in temp_tile:
            if row[0] == 'T':
                continue
            temp_puzzel[count%int(math.sqrt(len(puzzel)))].append(row)
        #print(temp_tile)
        
    for i in range(len(temp_puzzel)):
        for j in range(len(temp_puzzel[i])):
            if i == 0:
                big_puzzel.append(temp_puzzel[i][j])
            else:
                big_puzzel[j] = big_puzzel[j] + temp_puzzel[i][j]
    
    '''for i in big_puzzel:
        print(i)'''
    for row in range(len(sea_monster)):
        for char in range(len(sea_monster[row])):
            if sea_monster[row][char] == '#':
                coordinates.append((row, char))
    
    temp_coordinates = []
    for y, x in coordinates:
        temp_coordinates.append((y, x-18))
    coordinates = temp_coordinates
    print(coordinates)

    for row in range(len(big_puzzel)):
        for char in range(len(big_puzzel[row])):
            if big_puzzel[row][char] == '#':
                counter = 0
                for y, x in coordinates[1:]:
                    try:
                        if big_puzzel[row+y][char+x] == '#' and char+x >= 0:
                            #print(row+y, char+x, big_puzzel[row+y][char+x])
                            counter += 1
                        else:
                            break
                    except:
                        break
                print(counter)
                #print(y, x)
                #exit()
    print(len(coordinates))
    for i in big_puzzel:
        print(i)


puzzel = read_puzzle('try.txt')    
#puzzel = read_puzzle('day_20.txt')     
    
start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(puzzel), 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel_2(puzzel), 'solved in', time.perf_counter() - start, 'sec')