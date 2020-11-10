import json
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Receipe, Ingredients, IngredientsReceipe, User, Follow
from .forms import ReceipeForm
from .utils import get_ingredients, food_time_filter

@user_passes_test(lambda user: user.is_superuser)
def ingredients(request):
    with open("ingredients.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for ingr in data:
        ingredient = Ingredients(title=ingr["title"], dimension=ingr["dimension"])
        ingredient.save()
    return HttpResponse("\n".join(str(data)))

def index(request):
    receipe = Receipe.objects.select_related("author").order_by("-pub_date").all()
    receipe_list, food_time = food_time_filter(request, receipe)
    paginator = Paginator(receipe_list, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request, "index.html", {
            "page" : page,
            "paginator" : paginator,
            "food_time" : food_time,
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

def profile(request, username):
    user = request.user
    author = get_object_or_404(User, username=username)
    recipe = Receipe.objects.filter(author=author)
    recipe_list = recipe.order_by("-pub_date")
    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    if user.is_authenticated:
        following = Follow.objects.filter(user=request.user, author=author)
    else:
        following = False
    return render(request, "profile.html", {
        "author" : author,
        "page" : page,
        "paginator" : paginator,
        "following" : following,
    })

def recipe_view(request, username, recipe_id):
    author = get_object_or_404(User, username=username)
    recipe = get_object_or_404(Receipe, pk=recipe_id, author=author)
    ingredients = IngredientsReceipe.objects.filter(receipe=recipe)
    return render(request, "single_recipe.html", {
        "recipe" : recipe,
        "username" : author,
        "ingredients" : ingredients
    })

@login_required
def follow_index(request):
    follow = Follow.objects.filter(user=request.user)
    cnt = {}
    for author in follow:
        amount = Receipe.objects.filter(author=author.author).count()
        cnt[author.author] = amount
    paginator = Paginator(follow, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "follow.html", {
            "page" : page,
            "paginator" : paginator,
            "cnt" : cnt,
        }
    )

@login_required
def profile_follow(request, username):
    user = request.user
    author = get_object_or_404(User, username=username)
    exists = Follow.objects.filter(user=user, author=author).exists()
    if user != author and not exists:
        Follow.objects.create(user=user, author=author)
    return redirect("profile", username=author)

@login_required
def profile_unfollow(request, username):
    user = request.user
    author = get_object_or_404(User, username=username)
    follow = Follow.objects.filter(user=user, author=author)
    follow.delete()
    return redirect("profile", username=username)
