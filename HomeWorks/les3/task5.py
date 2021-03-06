"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков
(по одному слову из каждого списка):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
# >>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

def joke():

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    import random

    noun = random.choice(nouns)
    adverb = random.choice(adverbs)
    adjective = random.choice(adjectives)
    return f'{noun} {adverb} {adjective}'

def get_jokes(n):
    """
    Function returns jokes in list.
    :param n: quantity of jokes
    :return: list of jokes
    """
    jokes =[]
    for i in range(n):
        jokes.append(joke())
    return jokes



#    i = []
#    a = (random.choice(nouns) + random.choice(adverbs) + random.choice(adjectives))
#    i.append(a)
#    return i

# Нужно ли random оставялять вне функции, если мы к нему обращаемся внутри нее? Если поставим его в функцию она станет
# слишком тяжелой? Не понимаю, как это работает)

print(get_jokes(12))