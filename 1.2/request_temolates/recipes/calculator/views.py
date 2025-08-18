from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dish(request, recipe_name):
    if recipe_name not in DATA:
        context = {
            "description": f"Такого рецепта нет \"{recipe_name}\".",
            "recipe_names": list(DATA.keys())
        }

        return render(request, 'calculator/list.html', context)

    amount = int(request.GET.get("servings", 1))
    recipe = {k: v * amount for k, v in DATA[recipe_name].items()}

    context = {
        "recipe_name": recipe_name,
        "amount": amount,
        "recipe": recipe
    }

    return render(request, 'calculator/index.html', context)
