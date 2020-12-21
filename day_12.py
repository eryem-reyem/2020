import time

def get_puzzel_list(file):
    with open(file) as f:
        return [row.strip() for row in f]
puzzel = get_puzzel_list('day_12.txt')

def solve_puzzel_1(puzzel):
    directions_dict = {'north' : 0, 'east': 0, 'south' : 0, 'west' : 0}
    directions = {'north' : 0, 'east': 90, 'south' : 180, 'west' : 270}
    direction = 'east'

    for step in puzzel:
        move = step[0]
        value = int(step[1:])

        if move == 'N':
            directions_dict['north'] += value
        elif move == 'S':
            directions_dict['south'] += value
        elif move == 'E':
            directions_dict['east'] += value
        elif move == 'W':
            directions_dict['west'] += value
        elif move == 'R':
            new_direction = directions[direction] + value
            if new_direction >= 360:
                new_direction -= 360
            direction = [key  for (key, value) in directions.items() if value == new_direction][0]
        elif move == 'L':
            new_direction = directions[direction] - value
            if new_direction < 0:
                new_direction += 360
            direction = [key  for (key, value) in directions.items() if value == new_direction][0]
        elif move == 'F':
            directions_dict[direction] += value

    return abs(directions_dict['north']-directions_dict['south']) + abs(directions_dict['east']-directions_dict['west'])
        
def solve_puzzel_2(puzzel):
    directions_dict = {'north' : 0, 'east': 0, 'south' : 0, 'west' : 0}
    directions = {'north' : 0, 'east': 90, 'south' : 180, 'west' : 270}
    direction = 'east'
    waypoints = {'north' : 1, 'east': 10, 'south' : 0, 'west' : 0}

    def turn_waypoints(move, value, waypoints):
        temp_dict = {}

        if value == 90:
            if move == 'R':
                temp_dict['north'] = waypoints['west']
                temp_dict['east'] = waypoints['north']
                temp_dict['south'] = waypoints['east']
                temp_dict['west'] = waypoints['south']
            elif move == 'L':
                temp_dict['north'] = waypoints['east']
                temp_dict['east'] = waypoints['south']
                temp_dict['south'] = waypoints['west']
                temp_dict['west'] = waypoints['north']
                
        elif value == 180:
            if move == 'R':
                temp_dict['north'] = waypoints['south']
                temp_dict['east'] = waypoints['west']
                temp_dict['south'] = waypoints['north']
                temp_dict['west'] = waypoints['east']
            elif move == 'L':
                temp_dict['north'] = waypoints['south']
                temp_dict['east'] = waypoints['west']  
                temp_dict['south'] = waypoints['north']
                temp_dict['west'] = waypoints['east']

        elif value == 270:
            if move == 'R':
                temp_dict['north'] = waypoints['east']
                temp_dict['east'] = waypoints['south']
                temp_dict['south'] = waypoints['west']
                temp_dict['west'] = waypoints['north']
            elif move == 'L':
                temp_dict['north'] = waypoints['west']
                temp_dict['east'] = waypoints['north']  
                temp_dict['south'] = waypoints['east']
                temp_dict['west'] = waypoints['south']
        return temp_dict
            
    for step in puzzel:
        move = step[0]
        value = int(step[1:])

        if move == 'N':
            waypoints['north'] += value
        elif move == 'S':
            waypoints['south'] += value
        elif move == 'E':
            waypoints['east'] += value
        elif move == 'W':
            waypoints['west'] += value
        elif move == 'R':
            new_direction = directions[direction] + value
            if new_direction >= 360:
                new_direction -= 360
            direction = [key  for (key, value) in directions.items() if value == new_direction][0]
            waypoints = turn_waypoints(move, value, waypoints)
        elif move == 'L':
            new_direction = directions[direction] - value
            if new_direction < 0:
                new_direction += 360
            direction = [key  for (key, value) in directions.items() if value == new_direction][0]
            waypoints = turn_waypoints(move, value, waypoints)
        elif move == 'F':
            for i in directions:   
                directions_dict[i] += (waypoints[i]*value)
               
    return abs(directions_dict['north']-directions_dict['south']) + abs(directions_dict['east']-directions_dict['west'])

start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(puzzel), 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel_2(puzzel), 'solved in', time.perf_counter() - start, 'sec')