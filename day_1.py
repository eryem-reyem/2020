# https://adventofcode.com/2020/day/1

def read_puzzle(file):
    with open(file) as f:
        return [int(x) for x in f]

new_list = read_puzzle('day_1.txt')

print(new_list)

for i in new_list:
    for j in new_list:
         for k in new_list:
            if i+j+k == 2020:
                print(i * j * k)
                exit


