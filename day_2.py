# https://adventofcode.com/2020/day/2

def read_puzzle(file):
    with open(file) as f:
        return [x for x in f]

new_list = read_puzzle('day_2.txt')
passwort_count = 0

for i in new_list:
    a = i.split(':')
    int_1 = int(a[0].split('-')[0])
    int_2 = int(a[0].split(' ')[0].split('-')[1])
    letter = a[0].split(' ')[1]
    code = a[1][:-1]
    if code[int_1] == letter or code[int_2] == letter:
        if code[int_1] != code[int_2]:
            passwort_count += 1
    
    
    '''count = 0            #part one
    for i in code:
        if i == letter:
            count +=1
    if count >= int_1 and count <= int_2:
        passwort_count +=1'''

    #print(a, code, int_1, int_2, letter)
    #print(count)
    print(passwort_count)




