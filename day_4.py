# https://adventofcode.com/2020/day/4

'''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
'''
'''
if k == 'byr':
    1920 - 2002
elif k == 'iyr':
    2010 - 2020
elif k == 'eyr':
    2020 - 2030
elif k == 'hgt':
    cm = 150 - 193
    in_ = 59 - 76
elif k == 'hcl':
    'a # followed by exactly six characters 0-9 or a-f'
    pass
elif k == 'ecl':
    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
elif k == 'pid':
    'a nine-digit number, including leading zeroes'
    pass
'''

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

document = open('day_4.txt')

count = 0

new_list = [[]]
new_list_2 = []
for i in document:
    if i[:-1] == '':
        count += 1
        new_list.append([])
    else:
        new_list[count].append(i.replace('\n', ' '))

for i in new_list:
    new_list_2.append(' '.join(i))

valid_count = 0
for i in new_list_2:
    count_2 = 0
    for j in fields:
        if j in i:
            count_2 += 1
    if count_2 == 7:   
        count_3 = 0
        list_of_strings = i.split()
        for k in list_of_strings:
            if 'byr' in k:
                if len(k.partition(':')[2]) == 4:
                    if int(k.partition(':')[2]) >= 1920 and int(k.partition(':')[2]) <= 2002:
                        count_3 += 1
                    #print(k.partition(':')[2])
                #1920 - 2002
            elif 'iyr' in k:
                if len(k.partition(':')[2]) == 4:
                    if int(k.partition(':')[2]) >= 2010 and int(k.partition(':')[2]) <= 2020:
                        count_3 += 1
                #2010 - 2020
            elif 'eyr' in k:
                if len(k.partition(':')[2]) == 4:
                    if int(k.partition(':')[2]) >= 2020 and int(k.partition(':')[2]) <= 2030:
                        count_3 += 1
                #2020 - 2030
            elif 'hgt' in k:
                if 'in' in k:
                    if int(k.partition(':')[2].partition('in')[0]) >= 59 and int(k.partition(':')[2].partition('in')[0]) <= 76:
                        count_3 += 1
                        print(k)
                elif 'cm' in k:
                    if int(k.partition(':')[2].partition('cm')[0]) >= 150 and int(k.partition(':')[2].partition('cm')[0]) <= 193:
                        count_3 += 1  
                        print(k)             
                #cm = 150 - 193
                #in_ = 59 - 76
            elif 'hcl' in k:  
                b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
                hcl = k.partition('#')[2] 
                if len(hcl) == 6:
                    for element in hcl:
                        if element not in b:
                            break    
                    count_3 += 1
                    #'a # followed by exactly six characters 0-9 or a-f'
            elif 'ecl' in k:
                ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                for element in ecl_list:
                    if element in k:
                        count_3 +=1 
            elif 'pid' in k:
                if len(k.partition(':')[2]) == 9:
                    try:
                        #print(int(k.partition(':')[2])) 
                        count_3 += 1
                    except:
                        continue
                #'a nine-digit number, including leading zeroes'
            
            #if count_3 == 7:
                #print(i)
                #valid_count += 1 
    #print(list_of_strings)
    '''if count_2 == 7:
        valid_count += 1'''
#print(count_3)
print(valid_count)

