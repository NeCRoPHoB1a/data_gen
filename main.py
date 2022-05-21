import random


def time_gen(r):
    t1 = str(random.randint(r, 23))
    t2 = str(random.randint(0, 59))
    pp = ["0", ""]
    return pp[len(t1) - 1] + t1 + ":" + pp[len(t2) - 1] + t2


f = open('text.txt', 'w')

types = ["Особо большой", "Большой", "Средний", "Малый", "Особо малый"]
cities = ["Северодвинск", "Котлас", "Коряжма", "Новодвинск", "Мирный",
          "Вельск", "Онега", "Няндома",
          "Нарьян-Мар", "Каргополь", "Шенкурск", "Мезень", "Сольвычегодск"]

for i in range(21):
    f.write(str(random.randint(100, 999)) + '\n')
    f.write(random.choice(types) + '\n')
    f.write(str(random.choice(cities)) + '\n')
    f.write(time_gen(0) + '\n')
    f.write(time_gen(random.randint(1, 22)) + '\n')
    f.write('\n')
