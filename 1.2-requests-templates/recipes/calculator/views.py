from django.shortcuts import render
from django.http import HttpResponse

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
}

def omlet_view(request):
    omlet = DATA['omlet']
    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'
    list_ingredients = {}
    for ingredient, amount in omlet.items():   
        list_ingredients[ingredient] = amount * servings
    context = {
        'recipe': list_ingredients
    }
    return render(request, template_name, context)

def pasta_view(request):
    pasta = DATA['pasta']
    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'
    list_ingredients = {}
    for ingredient, amount in pasta.items():   
        list_ingredients[ingredient] = amount * servings
    context = {
        'recipe': list_ingredients
    }
    return render(request, template_name, context)

def buter_view(request):
    buter = DATA['buter']
    servings = int(request.GET.get('servings', 1))
    template_name = 'calculator/index.html'
    list_ingredients = {}
    for ingredient, amount in buter.items():   
        list_ingredients[ingredient] = amount * servings
    context = {
        'recipe': list_ingredients
    }
    return render(request, template_name, context)