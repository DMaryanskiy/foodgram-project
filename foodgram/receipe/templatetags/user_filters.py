from django import template

from receipe.models import Receipe

register = template.Library()

@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class" : css})

@register.filter
def get_recipes(author):
    return Receipe.objects.select_related("author").filter(author=author)[:3]

@register.filter
def get_count_recipes(author):
    count = author.recipes_author.count() - 3
    if count < 1:
        return False
    
    if count % 10 == 1 and count % 100 != 11:
        end = 'рецепт'
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
        end = 'рецепта'
    else:
        end = 'рецептов'

    return f'Еще {count} {end}...'

