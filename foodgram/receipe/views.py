import json
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Receipe, Ingredients, IngredientsReceipe, User
from .forms import ReceipeForm
from .utils import get_ingredients

def ingredients(request):
    with open("ingredients.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for ingr in data:
        ingredient = Ingredients(title=ingr["title"], dimension=ingr["dimension"])
        ingredient.save()
    return HttpResponse("\n".join(str(data)))

def index(request):
    receipe_list = Receipe.objects.order_by("-pub_date").all()
    paginator = Paginator(receipe_list, 6)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request, "index.html", {
            "page" : page,
            "paginator" : paginator,
        }
    )

@login_required
def add_receipe(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        ingr = get_ingredients(request)
        form = ReceipeForm(request.POST or None, files=request.FILES or None)
        if not ingr:
            form.add_error(None, 'Добавьте ингредиенты')

        elif form.is_valid():
            receipe = form.save(commit=False)
            receipe.author = user
            receipe.save()
            for ingr_name, amount in ingr.items():
                ingr_obj = get_object_or_404(Ingredients, title=ingr_name)
                ingr_receipe = IngredientsReceipe(
                    ingredient=ingr_obj,
                    receipe=receipe,
                    amount=amount,
                )
                ingr_receipe.save()
            form.save_m2m()
            return redirect("index")
    
    else:
        form = ReceipeForm()
    return render(request, "receipeform.html", {
        "form" : form,
    })

"""def profile(request):
    user = request.user
    author = get_object_or_404(User, username=username)
    recipe = Receipe.objects.filter(author=author)
    recipe_list = recipe.order_by("-pub_date")
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return """
