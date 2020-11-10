from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    IngredientListView,
    api_follow_detail
)

router = DefaultRouter()
router.register(r'ingredients', IngredientListView)

urlpatterns = [
    path('subscriptions/<author_id>', api_follow_detail),
]

urlpatterns += router.urls
