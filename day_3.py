# https://adventofcode.com/2020/day/3

imported_list = open('day_3.txt')
new_list = []
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]
position = 0
count = [0, 0, 0, 0, 0]

for i in imported_list:
    a = str(i)
    new_list.append(a)


for x in range(len(right)-1):
    position = 0
    for i in range(len(new_list)):
        if new_list[i][position] == '#':
            count[x] += 1
        position += right[x]
        
        if position >= 31:
            position -= 31

position = 0
for i in range(len(new_list)):
    if i%2 == 0:
        if new_list[i][position] == '#':
            count[4] += 1
        position += right[4]
        
        if position >= 31:
            position -= 31
            
position = 1    
    
#print(count)

for i in range(len(count)):
    position *= count[i]

print(position)