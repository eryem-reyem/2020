# https://adventofcode.com/2020/day/6

document = open('day_6.txt')
new_document = [[]]
group_count = 0
for i in document:
    if i == '\n':
        new_document.append([])
        group_count += 1
    else:
        new_document[group_count].append(i.replace('\n', ' '))

group_count = 0
result = 0
list_of_strings = []
for group in new_document:
    list_of_strings.append([])
    for persons in group:    
        for letter in persons:
            if letter != ' ':
                list_of_strings[group_count].append(letter)
    group_count += 1

new_list_of_strings = []
for group in list_of_strings:
    new_list_of_strings.append(''.join(group))

answered_yes = 0
answered_yes_list = []

for group in new_list_of_strings:
    
    answered_yes_list = []
    for i in group:
        if i not in answered_yes_list:
            answered_yes_list.append(i)
    answered_yes += len(answered_yes_list)

print(answered_yes)