import time
import itertools

def get_puzzel_list(file):
    with open(file) as f:
        return [row.strip() for row in f]
puzzel = get_puzzel_list('day_14.txt')


def solve_puzzel_1(puzzel):
    mask = ''
    results = {}

    def get_result(value, mask):
        new_value = []
        reversed_value = value[::-1]
       
        for i in range(len(mask)):
            if mask[i] == 'X' and i < len(mask) - len(value) :
                new_value.append('0')
            elif mask[i] != 'X':
                new_value.append(mask[i])
            else:
                new_value.append(reversed_value[len(mask)-i-1])

        return int('0b' + ''.join(new_value), 2)
       
    for i in puzzel:
        arg, value = i.split('=')
        
        if 'mask' in i:
            mask = value.strip()
        else:
            results[int(arg[4:-2])] = get_result(bin(int(value.strip()))[2:], mask)
    
    return sum(results.values())


def solve_puzzel_2(puzzel):
    mask = ''
    results = {}

    def get_binary(int_arg):
        return bin(int_arg)[2:]

    def floating(new_value):
        addr_string = ''.join(new_value)
        addrs = []
        number_of_x = new_value.count('X')
        
        for i in itertools.product([0, 1], repeat=number_of_x):
            new_addr = addr_string[:]
            for number in i:
                new_addr = new_addr.replace('X', str(number), 1)
            addrs.append(int('0b' + new_addr, 2))
            
        return addrs

    def check_mask(mask, binary):
        new_value = []
        reversed_value = binary[::-1]
        memory_adr = []

        for i in range(len(mask)):
            if mask[i] == '0' and i < len(mask) - len(reversed_value) :
                new_value.append('0')
            elif mask[i] == '1':
                new_value.append('1')
            elif mask[i] == 'X':
                new_value.append('X')
            else:
                new_value.append(reversed_value[len(mask)-i-1])
        
        return floating(new_value)


    for i in puzzel:
        arg, value = i.split('=')
        
        if 'mask' in i:
            mask = value.strip()
        else:
            addrs = check_mask(mask, get_binary(int(arg[4:-2])))
            for i in addrs:
                results[i] = int(value)

    return sum(results.values())


start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(puzzel), 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel_2(puzzel), 'solved in', time.perf_counter() - start, 'sec')