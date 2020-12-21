from typing import NamedTuple, Dict, List, Tuple
import re
from collections import defaultdict

document = open('day_7.txt')
RAW = ''.join(document)


class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]

def parse_line(line: str) -> Bag:
    part_1 , part_2 = line.split(' contain ')
    color = part_1[:-5]
    part_2 = part_2.rstrip('.')
    if part_2 == 'no other bags':
        return Bag(color, {})

    contains = {}
    
    contained = part_2.split(', ')
    for subbag in contained:
        subbag = re.sub(r'bags?$', '', subbag)
        first_space = subbag.find(' ')
        count = int(subbag[:first_space].strip())
        color_2 = subbag[first_space:].strip()
        contains[color_2] = count
    return Bag(color, contains)

def make_bags(raw: str) -> List[Bag]:
    return [parse_line(line) for line in raw.split('\n')]

def parents(bags: List[Bag]) -> Dict[str, List[str]]:
    ic = defaultdict(list)
    for bag in bags:
        for child in bag.contains:
            ic[child].append(bag.color)
    return ic

def can_contain(bags: List[Bag], color: str) -> List[str]:
    parent_map = parents(bags)

    check_me = [color]
    can_contain = set()

    while check_me:
        child = check_me.pop()
        for parent in parent_map.get(child, []):
            if parent not in can_contain:
                can_contain.add(parent)
                check_me.append(parent)

    return list(can_contain)
  
bags =  make_bags(RAW)

print(len(can_contain(bags, 'shiny gold')))