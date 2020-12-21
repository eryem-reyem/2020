document = open('day_8.txt')
result = 0
new_list = []
for i in document:
    new_list.append([i.split(' ')[0], False, int(i.split(' ')[1].rstrip('\n'))])


def run_program(new_list):
    global result
    count = 0
    position = new_list[count]
    instruction = position[0]
    is_visited = position[1]
    steps = position[2]
    
    while True:
        if new_list[count][1] == True:
                break

        if new_list[count][0] == 'nop':
            new_list[count][1] = True
            count += 1   
            
        elif new_list[count][0] == 'acc':
            new_list[count][1] = True
            result += new_list[count][2]
            count += 1
            
        elif new_list[count][0] == 'jmp':
            new_list[count][1] = True
            count += new_list[count][2]        
   
run_program(new_list)
print(result)