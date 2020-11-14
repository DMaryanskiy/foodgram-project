from rest_framework import serializers

from receipe.models import Ingredients, Follow, Favourite, Purchase


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["title", "dimension", ]
        model = Ingredients


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        fields = "__all__"
        model = Follow


class FavouriteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    recipe = serializers.StringRelatedField()

    class Meta:
        fields = "__all__"
        model = Favourite


class PurchaseSerializer(serializers.ModelSerializer):
    buyer = serializers.StringRelatedField()
    recipe = serializers.StringRelatedField()

    class Meta:
        fields = "__all__"
        model = Purchase
