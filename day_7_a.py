document = open('try.txt')
new_document = []
for row in document:
    new_document.append(row.replace('\n', ' '))
contain_dict = {}
searched_contain = 'shiny gold'
list_of_containing_bags = []

def get_dict(doc):
    for i in doc:
        part_1 = i.split(' bags contain ')[0]
        part_2 = i.split(' bags contain ')[1].rsplit('.')[0].rsplit(', ')
        #print(part_2)
        temp_dict = {}
        
        if 'no other bags' not in i:
            for i in part_2:          
                temp_dict[i[2:].split(' bag')[0]] = int(i.split(' ')[0])
            contain_dict[part_1] = temp_dict

def get_containing_bags(doc):
    get_dict(doc)
    for bag, contain in contain_dict.items():
        if searched_contain in contain:
            list_of_containing_bags.append(bag)
    for bag, contain in contain_dict.items():
        for i in list_of_containing_bags:
            if i in contain and bag not in list_of_containing_bags:
                list_of_containing_bags.append(bag)

get_containing_bags(new_document)


for i in new_document:
    print(i)



    #print(part_1, part_2)
