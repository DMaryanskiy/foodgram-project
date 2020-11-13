from django import template

from receipe.models import Recipe, Favourite, Follow, Purchase

register = template.Library()

@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class" : css})

@register.filter(name="get_recipes")
def get_recipes(author):
    return Recipe.objects.select_related("author").filter(author=author)[:3]

@register.filter(name="get_count_recipes")
def get_count_recipes(author):
    count = author.recipes.count() - 3
    if count < 1:
        return False
    
    if count % 10 == 1 and count % 100 != 11:
        end = 'рецепт'
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
        end = 'рецепта'
    else:
        end = 'рецептов'

    return f'Еще {count} {end}...'

@register.filter(name="is_favourite")
def is_favourite(recipe, user):
    return Favourite.objects.select_related("recipe").filter(
        user=user,
        recipe=recipe,
    ).exists()

@register.filter(name="is_following")
def is_following(author, user):
    return Follow.objects.select_related("author").filter(
        author=author,
        user=user
    ).exists()

@register.filter(name="is_purchase")
def is_purchase(recipe, buyer):
    if not buyer.is_authenticated:
        return False
    return Purchase.objects.select_related("recipe").filter(
        buyer=buyer,
        recipe=recipe,
    ).exists()
