import time

def get_puzzel_list(file):
    with open(file) as f:
        return [row.strip() for row in f]
puzzel = get_puzzel_list('day_16.txt')


def split_puzzel(puzzel):
    values = {}
    my = []
    nearby = []
    count = 0
    nearby_count = 0

    for line in puzzel:
        if 'or' in line:
            temp_list = []
            values[line.split(':')[0].strip()] = line.split(':')[1].split('or')
            for i in values[line.split(':')[0].strip()]:
                a = int(i.strip().split('-')[0])
                b = int(i.strip().split('-')[1])
                for j in range(a, b+1):
                    temp_list.append(j)
            values[line.split(':')[0].strip()] = temp_list

        if count == 1 and ',' in line:
            for i in line.split(','):
                my.append(int(i))
        elif count == 2 and ',' in line: 
            nearby.append([])
            for i in line.split(','):
                nearby[nearby_count].append(int(i))
            nearby_count += 1

        if 'your' in line:
            count += 1
        elif 'nearby' in line:
            count += 1

    return values, nearby, my;


def solve_puzzel_1(puzzel):
    split = split_puzzel(puzzel)
    values = split[0]
    nearby = split[1]
    my = split[2]
    lost_values = []
    all_values = []

    for j in values.values():
        for i in j:
            all_values.append(i)

    for i in nearby:
        for j in i:
            if j not in all_values:
                lost_values.append(j)
    
    return sum(lost_values)


def solve_puzzel_2(puzzel):
    values, nearby,  my= split_puzzel(puzzel)
    unvalid_tickets = []
    valid_tickets = []
    possibel_rules = {}
    list_of_rules = []
    result = 1

    for ticket in nearby:
        for number in ticket:
            counter = 0
            for rule in values.values():
                if number not in rule:
                    counter += 1
                if counter == 19:
                    unvalid_tickets.append(ticket)
                    break
        
    for ticket in nearby:
        if ticket not in unvalid_tickets:
            valid_tickets.append(ticket)            
    
    for rule in values:
        list_of_rules.append(rule)
    for i in range(20):
        possibel_rules[i] = list_of_rules

    for ticket in valid_tickets:
        for count, number in enumerate(ticket):
            for rule in values:
                
                if number not in values[rule] and rule in possibel_rules[count]:
                    temp_list = possibel_rules[count][:]
                    temp_list.remove(rule)
                    possibel_rules[count] = temp_list

    while True:
        count = 0

        for i in possibel_rules:
            if len(possibel_rules[i]) == 1:
                count += 1
                for j in possibel_rules:
                    if len(possibel_rules[j]) != 1 and possibel_rules[i][0] in possibel_rules[j]:
                        temp_list = possibel_rules[j][:]
                        temp_list.remove(possibel_rules[i][0])
                        possibel_rules[j] = temp_list
        if count ==  20:
            break
    
    for i in possibel_rules:
        if 'departure' in possibel_rules[i][0]:
            result *= my[i]

    return result

        
start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(puzzel), 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel_2(puzzel), 'solved in', time.perf_counter() - start, 'sec')