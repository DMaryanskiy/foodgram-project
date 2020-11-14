from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import HttpResponse

from .models import (
    Recipe,
    Ingredients,
    IngredientsRecipe,
    User,
    Follow,
    Purchase,
)
from .forms import RecipeForm
from .utils import get_ingredients, food_time_filter


def index(request):
    recipe = Recipe.objects.select_related(
        "author"
    ).order_by("-pub_date").all()
    recipe_list, food_time = food_time_filter(request, recipe)
    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request, "index.html", {
            "page": page,
            "paginator": paginator,
            "food_time": food_time,
        }
    )


@login_required
def add_recipe(request):
    user = User.objects.get(username=request.user)
    if request.method == "POST":
        ingr = get_ingredients(request)
        form = RecipeForm(request.POST or None, files=request.FILES or None)
        if not ingr:
            form.add_error(None, 'Добавьте ингредиенты')

        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = user
            recipe.save()
            for ingr_name, amount in ingr.items():
                ingr_obj = get_object_or_404(Ingredients, title=ingr_name)
                ingr_recipe = IngredientsRecipe(
                    ingredient=ingr_obj,
                    recipe=recipe,
                    amount=amount,
                )
                ingr_recipe.save()
            form.save_m2m()
            return redirect("index")

    else:
        form = RecipeForm()
    return render(request, "recipeform.html", {
        "form": form,
    })


def profile(request, username):
    author = get_object_or_404(User, username=username)
    recipe = Recipe.objects.select_related("author").filter(author=author)
    recipe_list, food_time = food_time_filter(request, recipe)
    recipe_list = recipe_list.order_by("-pub_date")
    paginator = Paginator(recipe_list, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "profile.html", {
        "author": author,
        "page": page,
        "paginator": paginator,
        "food_time": food_time,
    })


def recipe_view(request, username, recipe_id):
    author = get_object_or_404(User, username=username)
    recipe = get_object_or_404(Recipe, pk=recipe_id, author=author)
    ingredients = IngredientsRecipe.objects.filter(recipe=recipe)
    return render(request, "single_recipe.html", {
        "recipe": recipe,
        "username": author,
        "ingredients": ingredients,
    })


@login_required
def recipe_edit(request, username, recipe_id):
    change = True
    profile = get_object_or_404(User, username=username)
    recipe = get_object_or_404(Recipe, pk=recipe_id, author=profile)
    ingr_objects = IngredientsRecipe.objects.filter(recipe=recipe)

    if request.method == "POST":
        ingr = get_ingredients(request)
        form = RecipeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=recipe,
        )

        if not ingr_objects:
            form.add_error(None, "Добавьте ингредиенты!")

        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()
            IngredientsRecipe.objects.filter(recipe=recipe).delete()

            for ingr_name, amount in ingr.items():
                ingr_obj = get_object_or_404(Ingredients, title=ingr_name)
                ingr_recipe = IngredientsRecipe(
                    ingredient=ingr_obj,
                    recipe=recipe,
                    amount=amount,
                )
                ingr_recipe.save()
            form.save_m2m()
            return redirect("index")

    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipeform.html", {
        "form": form,
        "recipe": recipe,
        "ingr": ingr_objects,
        "change": change,
    })


@login_required
def recipe_delete(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    user = request.user

    if request.method == "POST":
        author = get_object_or_404(User, username=username)
        if recipe.author == author == user or user.is_superuser:
            recipe.delete()
        return redirect("index")
    else:
        return render(request, "delete_submit.html", {
            "recipe_id": recipe_id,
            "username": username,
            "recipe": recipe,
        })


@login_required
def follow_index(request):
    follow = Follow.objects.filter(user=request.user)
    cnt = {}
    for author in follow:
        amount = Recipe.objects.filter(author=author.author).count()
        cnt[author.author] = amount
    paginator = Paginator(follow, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "follow.html", {
            "page": page,
            "paginator": paginator,
            "cnt": cnt,
        }
    )


@login_required
def favourite_index(request):
    recipe = Recipe.objects.select_related("author").filter(
        recipe_favourite__user__pk=request.user.id)
    recipes, food_time = food_time_filter(request, recipe)
    paginator = Paginator(recipes, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "favourite.html", {
            "page": page,
            "paginator": paginator,
            "food_time": food_time,
        }
    )


@login_required
def purchase_list(request):
    recipes = Purchase.objects.filter(buyer=request.user)
    return render(request, "shop_list.html", {
        "recipes": recipes,
    })


@login_required
def upload(request):
    recipes = Recipe.objects.filter(pur_recipe__buyer=request.user)
    ingredients = recipes.values(
        "ingredient_list__title",
        "ingredient_list__dimension",
    ).annotate(
        total_amount=Sum("recipe__amount")
    )
    file_data = ""

    for i in ingredients:
        line = " ".join(str(value) for value in i.values())
        file_data += line + "\n"

    response = HttpResponse(
        file_data,
        content_type="application/text charset=utf-8",
    )
    response["Content-Disposition"] = "attachment; filename='products.txt'"
    return response
