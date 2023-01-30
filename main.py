# Задание 1

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        food_amount = int(file.readline().strip())
        food = []
        for i in range(food_amount):
            fd = file.readline().strip()
            ingredient_name, quantity, measure = fd.split(' | ')
            food.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure

            })
        file.readline()
        cook_book[dish] = food
print(cook_book)

#Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    dish_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                dish_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
    return dish_list
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(result)

#Задание 3

dict_key = {}  # создаем словарь где имя файла это ключ, а кол-во строк в файле это значение

with open('1.txt', 'rt', encoding='utf-8') as file:
    name = '1.txt'
    sum_str = len(file.readlines())
    dict_key.setdefault(name, sum_str)


with open('2.txt', 'rt', encoding='utf-8') as file:
    name = '2.txt'
    sum_str = len(file.readlines())
    dict_key.setdefault(name, sum_str)

with open('3.txt', 'rt', encoding='utf-8') as file:
    name = '3.txt'
    sum_str = len(file.readlines())
    dict_key.setdefault(name, sum_str)


sorted_tuple = sorted(dict_key.items(), key=lambda x: x[1]) # переводим наш словарь в кортеж
sorted_dict = {k: v for k, v in sorted_tuple} # сортированный словарь по возрастанию
print(sorted_dict)

dict_text = {}  # создаем словарь где имя файла это ключ, а текст в файле это значение

with open('1.txt', 'rt', encoding='utf-8') as file:
    name = '1.txt'
    text_content = []
    for line in file:
        text_content.append(line.strip() + '\n')
        dict_text[name] = text_content
    dict_text.setdefault(name, text_content)


with open('2.txt', 'rt', encoding='utf-8') as file:
    name = '2.txt'
    text_content = []
    for line in file:
        text_content.append(line.strip() + '\n')
        dict_text[name] = text_content
    dict_text.setdefault(name, text_content)


with open('3.txt', 'rt', encoding='utf-8') as file:
    name = '3.txt'
    text_content = []
    for line in file:
        text_content.append(line.strip() + '\n')
        dict_text[name] = text_content
    dict_text.setdefault(name, text_content)

print(dict_text)

with open('Full_text.txt', 'w', encoding='utf-8') as f:
    for key in sorted_dict.keys():
        f.write(str(key) + '\n')
        f.write(str(sorted_dict[key]) + '\n')
        f.write("".join(map(str, dict_text[key])) + '\n')
        f.write('\n')
