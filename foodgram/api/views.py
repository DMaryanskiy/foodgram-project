from rest_framework import mixins, viewsets, filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.utils import IntegrityError

from .serializers import (
    IngredientSerializer,
    FollowSerializer,
    FavouriteSerializer,
)
from receipe.models import Ingredients, Follow, User, Receipe, Favourite


class IngredientListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", ]

@api_view(["POST", "DELETE"])
def api_follow_detail(request, author_id):
    author = generics.get_object_or_404(User, pk=author_id)
    if request.method == "POST":
        serializer = FollowSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(user=request.user, author=author)
            except IntegrityError:
                Response({"success" : False}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success" : True}, status=status.HTTP_201_CREATED)
        return  Response({"success" : False}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        follow = generics.get_object_or_404(Follow, user=request.user, author=author)
        follow.delete()
        return Response({"success" : True}, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST", "DELETE"])
def api_favourite_detail(request, recipe_id):
    recipe = generics.get_object_or_404(Receipe, pk=recipe_id)
    if request.method == "POST":
        serializer = FavouriteSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(user=request.user, recipe=recipe)
            except IntegrityError:
                Response({"success" : False}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"success" : True}, status=status.HTTP_201_CREATED)
        return Response({"success" : False}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        favourite = generics.get_object_or_404(
            Favourite,
            user=request.user,
            recipe=recipe
        )
        favourite.delete()
        return Response({"success" : True}, status=status.HTTP_204_NO_CONTENT)
