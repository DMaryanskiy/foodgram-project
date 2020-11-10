from rest_framework import mixins, viewsets, filters, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db.utils import IntegrityError

from .serializers import IngredientSerializer, FollowSerializer
from receipe.models import Ingredients, Follow, User


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
