import time

def solve_puzzel_1(repeats):
    puzzel = '1,2,16,19,18,0'
    puzzel = puzzel.split(',')
    puzzel_dict = {}
    for i in range(len(puzzel)):
        puzzel_dict[int(puzzel[i])] = [i+1]
    
    def get_key(val):
        for key, value in puzzel_dict.items():
            for x in value:
                if val == x:
                    return key  
        return "key doesn't exist"

    last_move = max(puzzel_dict.values())[0]
    last_move_key = get_key(last_move)
    result = 0

    for i in range(len(puzzel_dict)+1, repeats + 1, 1):
        if len(puzzel_dict[last_move_key]) == 1 : 
            result = 0
        else:
            result = puzzel_dict[last_move_key][-1] - puzzel_dict[last_move_key][-2]

        last_move += 1
        last_move_key = result

        if result in puzzel_dict.keys():
            puzzel_dict[result].append(i)
        else:
            puzzel_dict[result] = [i]
    return result

    
    
start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(2020), '- solved in', time.perf_counter() - start, 'sec') 

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel_1(30000000), '- solved in', time.perf_counter() - start, 'sec') 