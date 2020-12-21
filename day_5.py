# https://adventofcode.com/2020/day/5

rows = [0, 127]
columns = [0, 7]
data = []
seat_ids = []
document = open('day_5.txt')
new_list = []
for i in document:
    new_list.append(i.replace('\n', ' '))

for i in new_list: 
    rows = [0, 127]
    columns = [0, 7]
    for j in i:    
        if j == 'F':
            rows[1] = rows[1] - (rows[1] - rows[0])//2-1         
        if j == 'B':
            rows[0] = rows[0] + (rows[1] - rows[0])//2+1
        
        if j == 'L':
             columns[1] = columns[1] - (columns[1] - columns[0])//2-1  
        if j == 'R':
            columns[0] = columns[0] + (columns[1] - columns[0])//2+1
    seat_id = rows[0] * 8 + columns[0]
    data.append([rows[0], columns[0], seat_id])
       
for i in data:
    seat_ids.append(i[2])

print(sorted(seat_ids))

for i in range(75, 864):
    if i in seat_ids:
        continue
    else:
        print(i)