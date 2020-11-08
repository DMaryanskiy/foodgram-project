from django.contrib import admin

from .models import (
    Ingredients,
    IngredientsReceipe,
    Receipe
)


class IngredientsReceipeInLine(admin.TabularInline):
    model = IngredientsReceipe
    extra = 1


class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "dimension",
    )
    list_filter = ("title", )
    inlines = (IngredientsReceipeInLine, )


class IngredientsReceipeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "ingredient",
        "amount",
    )

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

admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(IngredientsReceipe, IngredientsReceipeAdmin)
admin.site.register(Receipe, ReceipeAdmin)
