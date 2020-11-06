from django.contrib import admin

from .models import (
    Ingredients,
    IngredientsReceipe,
    Tag,
    Receipe
)


class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "dimension",
    )
    list_filter = ("title", )


class IngredientsReceipeAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "ingredient",
        "amount",
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )


class ReceipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )
    list_filter = (
        "author",
        "title",
        "tag",
    )

admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(IngredientsReceipe, IngredientsReceipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Receipe, ReceipeAdmin)
