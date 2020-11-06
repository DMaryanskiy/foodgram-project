import json
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from .models import Receipe, Ingredients

def ingredients(request):
    with open("ingredients.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for ingr in data:
        ingredient = Ingredients(title=ingr["title"], dimension=ingr["dimension"])
        ingredient.save()
    return HttpResponse("\n".join(str(data)))