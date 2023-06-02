from django.shortcuts import render
from .models import Recipe

def main_view(request):
    recipes = Recipe.objects.filter(year=2023)
    return render(request, 'main.html', {'recipes': recipes})

def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
