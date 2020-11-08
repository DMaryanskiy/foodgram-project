from rest_framework import serializers

from receipe.models import Ingredients


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["title", "dimension", ]
        model = Ingredients
