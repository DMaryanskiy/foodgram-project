import json
from django.core.management.base import BaseCommand
from django.http import HttpResponse

from receipe.models import Ingredients

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("ingredients.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for ingr in data:
            ingredient = Ingredients(title=ingr["title"], dimension=ingr["dimension"])
            ingredient.save()
        return HttpResponse("\n".join(str(data)))
