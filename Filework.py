from pprint import pprint

#ЗАДАЧА 1

def get_dict(file):
    res = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            try:
                i = int(line.strip())
            except:
                key = line.strip()
            else:
                lines = []
                for data in range(i):
                    data = f.readline().strip()
                    lines.append(data)
                    res[key] = lines
            continue
    return res

def get_nice_dict(file):
    res = {}
    dict = get_dict(file)
    for k, v in dict.items():
        list = []
        for data in v:
            temp = {}
            ds = data.split(' | ')
            temp['ingredient_name'] = ds[0]
            temp['quantity'] = ds[1]
            temp['measure'] = ds[2]
            list.append(temp)
        res.setdefault(k, list)
    return res

#ЗАДАЧА 2

def get_shop_list_by_dishes(file, dishes, person_count):
    dict = get_nice_dict(file)
    res = {}
    for i in dishes:
        temp = dict.get(i, 'Ошибка')
        for j in temp:
            key = j.get('ingredient_name')
            qua = j.get('quantity')
            mea = j.get('measure')
            a = {}
            try:
                key == res[key]
            except:
                a['measure'] = mea
                res.setdefault(key, {}).update(a)
                a['quantity'] = (int(qua) * person_count)
                res.setdefault(key, {}).update(a)
            else:
                a['measure'] = mea
                res.setdefault(key, {}).update(a)
                b = res[key]['quantity']
                a['quantity'] = (b + int(qua) * person_count)
                res.setdefault(key, {}).update(a)
    return res

#ЗАДАЧА 3

def get_file(files):
    res = {}
    for file in files:
        with open(file, encoding='utf-8') as f:
            for i, list in enumerate(f):
                res[file] = (i + 1)
    with open('res.txt', 'w', encoding='utf-8') as fw:
        while res != {}:
            max_val = max(res.values())
            sort_dict = {k:v for k, v in res.items() if v == max_val}
            for key, value in sort_dict.items():
                fw.write(f'{key} \n')
                fw.write(f'{str(value)} \n')
                with open(key, encoding='utf-8') as fr:
                    for i, list in enumerate(fr):
                        fw.write(f'{list} - строка № {i} файла № {key} \n')
            fw.write('\n')
            del res[key]
    print('Успешная запись')


if __name__ == '__main__':
    print('Задание 1: \n')
    cook_book = get_nice_dict('recipes.txt')
    pprint(f'cook_book = {cook_book}')
    print('\nЗадание 2: \n')
    shoplist = get_shop_list_by_dishes('recipes.txt', ['Запеченный картофель', 'Омлет', 'Омлет', 'Омлет', 'Омлет', 'Омлет'], 5)
    pprint(shoplist)
    print('\nЗадание 3: \n')
    get_file(['1.txt', '2.txt', '3.txt', '4.txt', '5.txt'])
