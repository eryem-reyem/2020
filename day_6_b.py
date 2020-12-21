# https://adventofcode.com/2020/day/6

document = open('day_6.txt')
new_document = [[]]
group_count = 0
result = 0
for i in document:
    if i == '\n':
        new_document.append([])
        group_count += 1
    else:
        new_document[group_count].append(i.replace('\n', ' '))


for group in new_document:
    temp_dict = {}
    for i in range(len(group)):
        #print(group)
        for j in group[0]:
            if j != ' ':
                if j in group[i]:
                    if j not in temp_dict:
                        temp_dict[j] = 1
                    else:
                        temp_dict[j] += 1
                    #print(j)
        print(temp_dict)
        for key in temp_dict:
            if temp_dict[key] == len(group):
                result += 1
print(result)