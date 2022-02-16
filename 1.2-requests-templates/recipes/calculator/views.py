from django.shortcuts import render

import re

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def menu(request, name):
    servings = request.GET.get('servings')
    if servings == None:
        servings = '1/'
    servings = servings[:-1]
    ingredient_dict = {}
    for key, value in DATA[name].items():
        ingredient_dict[key] = value * int(servings)
    context = {
   'recipe': ingredient_dict,
   'servings' : servings
    }
    return render(request, 'calculator/index.html', context)