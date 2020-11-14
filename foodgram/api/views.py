from rest_framework import mixins, viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import (
    IngredientSerializer,
    FollowSerializer,
    FavouriteSerializer,
    PurchaseSerializer,
)
from receipe.models import (
    Ingredients,
    Follow,
    User,
    Recipe,
    Favourite,
    Purchase,
)


class IngredientListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", ]


@api_view(["POST", "DELETE"])
def api_follow_detail(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    if request.method == "POST":
        serializer = FollowSerializer(data=request.data, context={
            "request_user": request.user,
            "request_author": author,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, author=author)
        return Response({"success": True}, status=status.HTTP_201_CREATED)

    if request.method == "DELETE":
        get_object_or_404(
            Follow,
            user=request.user,
            author=author
        ).delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST", "DELETE"])
def api_favourite_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == "POST":
        serializer = FavouriteSerializer(data=request.data, context={
            "request_user": request.user,
            "request_recipe": recipe,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, recipe=recipe)
        return Response({"success": True}, status=status.HTTP_201_CREATED)

    if request.method == "DELETE":
        get_object_or_404(
            Favourite,
            user=request.user,
            recipe=recipe
        ).delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST", "DELETE"])
def api_purchase_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == "POST":
        serializer = PurchaseSerializer(data=request.data, context={
            "request_user": request.user,
            "request_recipe": recipe,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save(buyer=request.user, recipe=recipe)
        return Response({"success": True}, status=status.HTTP_201_CREATED)

    if request.method == "DELETE":
        get_object_or_404(
            Purchase,
            buyer=request.user,
            recipe=recipe
        ).delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
