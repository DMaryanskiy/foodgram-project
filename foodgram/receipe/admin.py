from django.contrib import admin

from .models import (
    Ingredients,
    IngredientsReceipe,
    Receipe
)


class IngredientsReceipeInLine(admin.TabularInline):
    model = IngredientsReceipe
    extra = 1


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "dimension",
    )
    list_filter = ("title", )
    inlines = (IngredientsReceipeInLine, )


@admin.register(IngredientsReceipe)
class IngredientsReceipeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "ingredient",
        "amount",
    )


@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )
    list_filter = (
        "author",
        "title",
    )
    inlines = (IngredientsReceipeInLine, )
