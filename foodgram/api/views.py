from rest_framework import mixins, viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import IngredientSerializer
from receipe.models import Ingredients


class IngredientListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", ]
