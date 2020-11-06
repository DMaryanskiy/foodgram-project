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

def index(request):
    receipe_list = Receipe.objects.order_by("-pub_date").all()
    paginator = Paginator(receipe_list, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request, "index.html", {
            "page" : page,
            "paginator" : paginator,
        }
    )