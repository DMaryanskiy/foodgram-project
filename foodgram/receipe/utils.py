from django.shortcuts import get_object_or_404, render
from django.forms import ValidationError

from .models import Ingredients

def get_ingredients(request):
    ingredients = {}
    for key in dict(request.POST.items()):
        if "nameIngredient" in key:
            a = key.split("_")
            if a[1].isdigit():
                ingredients[dict(request.POST.items())[key]] = int(request.POST[
                    f"valueIngredient_{a[1]}"]
                )
            else:
                raise ValidationError("Количество ингредиентов должно быть числом!")
    return ingredients
