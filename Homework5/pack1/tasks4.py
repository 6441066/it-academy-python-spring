

# 1. Dict comprehensions
# Создайте словарь с помощью генератора словарей, так чтобы его ключами
# были числа от 1 до 20, а значениями кубы этих чисел.
def dict_comprehensions():
    dict = {el: el ** 3 for el in range(1, 21)}
    return dict


# -----------------------------------------------------------------------------
# 2 Города
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
# Входные данные
# Программа получает на вход количество стран N. Далее идет N строк,
# каждая строка начинается с названия страны, затем идут названия
# городов этой страны. В следующей строке записано число M, далее
# идут M запросов — названия каких-то M городов, перечисленных выше.
# Выходные данные
# Для каждого из запроса выведите название страны,
# в котором находится данный город.
def cities(str_country_cities):
    list_str = str_country_cities.split("\n")
    dict_cities = dict()
    list_countrys = ["нет страны для города в базе данных."]
    n = 0
    for stroka in list_str:
        if stroka.isdigit():
            if n > 0:
                n = -1
        elif n > 0 and stroka:
            lists = stroka.split()
            for inds, s in enumerate(lists):
                if inds == 0:
                    list_countrys.append(s)
                else:
                    dict_cities[s] = n
        elif stroka:
            print(stroka, " => ", list_countrys[dict_cities.get(stroka, 0)])
        if n >= 0:
            n += 1


# -----------------------------------------------------------------------------
# 3
# Даны два списка чисел. Посчитайте, сколько различных чисел содержится
# одновременно как в первом списке, так и во втором.
def two_list(strs):
    str1, str2 = strs.split(",")
    set1 = set(str1.split())
    set1.update(set(str2.split()))
    print(len(set1))


# -----------------------------------------------------------------------------
# 4
# Даны два списка чисел. Посчитайте, сколько различных чисел
# входит только в один из этих списков
def count_different(strs):
    str1, str2 = strs.split(",")
    set1 = set(str1.split())
    set1.difference_update(set(str2.split()))
    print(set1)


# -----------------------------------------------------------------------------
# 5
# Слова
# Во входной строке записан текст. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
def words(stroka):
    print(len(stroka.replace("\n", ' ').split()))


varvar = 112
