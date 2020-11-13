from django.contrib import admin

from .models import (
    Ingredients,
    IngredientsRecipe,
    Recipe,
    Follow,
    Favourite,
)


class IngredientsRecipeInLine(admin.TabularInline):
    model = IngredientsRecipe
    extra = 1


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "dimension",
    )
    list_filter = ("title", )
    inlines = (IngredientsRecipeInLine, )


@admin.register(IngredientsRecipe)
class IngredientsRecipeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "ingredient",
        "amount",
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )
    list_filter = (
        "author",
        "title",
    )
    inlines = (IngredientsRecipeInLine, )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "author",
    )
    list_filter = (
        "user",
    )


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "recipe",
    )
    list_filter = (
        "user",
    )
