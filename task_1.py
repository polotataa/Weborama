import pandas as pd

# Чтение CSV файла без заголовка
data = pd.read_csv('table.csv', header=None, names=['cache', 'id'], dtype={'id': str})

# Создание списка из всех значений столбца 'id'
id_list = data['id'].tolist()

# Вывод списка id
#print(len(id_list))

# Создание словаря с подсчетом повторений id
count_dict = {}
for el in id_list:
    count_dict[el] = count_dict.get(el, 0) + 1

# Вывод id, которые встречаются только 3 раза
count_3times = [el for el, count in count_dict.items() if count == 3]
#print(len(count_3times))
print(*count_3times)


# Получение частоты повторений идентификаторов
# Создание словаря с подсчетом частоты повторений
freq_dict = {}
for count in count_dict.values():
    freq_dict[count] = freq_dict.get(count, 0) + 1

# Вывод частоты повторений
for count, freq in freq_dict.items():
    print("Количество повторений {}: {}".format(count, freq))
