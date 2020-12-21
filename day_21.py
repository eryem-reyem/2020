import time

def read_puzzle(file):
  with open(file) as f:
    return [row.strip() for row in f]


def get_list_of_food(puzzel):
    foods = []

    for row in puzzel:
        parts = row.split("(contains ")         
        foods.append([parts[0].split(), parts[1][:-1].split(", ")])  # [ingredients, allergens]

    return foods


def get_possible_ingredients(foods):
    poosibel_ingredients ={} 

    for food in foods:
        for allergen in food[1]:
            if allergen not in poosibel_ingredients:
                poosibel_ingredients[allergen] = set(food[0])
            else:
                temp = poosibel_ingredients[allergen].copy().intersection(set(food[0]))
                poosibel_ingredients[allergen] = temp

    return poosibel_ingredients


def get_known_ingredient(poosibel_ingredients):
    known_ingredient = {}

    while True:
        if len(poosibel_ingredients) == 0:
            break

        for i in poosibel_ingredients:
            if len(poosibel_ingredients[i]) == 1:
                known_ingredient[i] = poosibel_ingredients[i]
                del poosibel_ingredients[i]
                for j in known_ingredient:
                    for k in poosibel_ingredients:
                        poosibel_ingredients[k] = poosibel_ingredients[k].copy().difference(known_ingredient[j])
                break
        
    return known_ingredient


def solve_puzzel_1(puzzel):
    foods = get_list_of_food(puzzel)
    poosibel_ingrdients = get_possible_ingredients(foods)
    known_ingredient = get_known_ingredient(poosibel_ingrdients)
    count = 0
    known_values = []

    for value in known_ingredient.values():
        known_values.append(list(value)[0])

    for row in foods:
        for ingredient in row[0]:
            
            if ingredient not in known_values:
                count += 1
        
    return count, known_ingredient
        

def solve_puzzel_2(puzzel):
    known_ingredient = get_known_ingredient(get_possible_ingredients(get_list_of_food(puzzel)))     
    keys = []
    sorted_ingredients = []
        
    for key in known_ingredient.keys():
        keys.append(key)
    keys = sorted(keys)

    for key in keys:
        sorted_ingredients.append(list(known_ingredient[key])[0])

    return ','.join(sorted_ingredients)


puzzel = read_puzzle('day_21.txt')

start = time.perf_counter()
print('solution puzzel one:', '\t', solve_puzzel_1(puzzel)[0], 'solved in', time.perf_counter() - start, 'sec')

start = time.perf_counter()
print('solution puzzel two:', '\t', solve_puzzel_2(puzzel), 'solved in', time.perf_counter() - start, 'sec')