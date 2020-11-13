from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    IngredientListView,
    api_follow_detail,
    api_favourite_detail,
    api_purchase_detail,
)

router = DefaultRouter()
router.register(r'ingredients', IngredientListView)

urlpatterns = [
    path('subscriptions/<author_id>', api_follow_detail),
    path('favourites/<recipe_id>', api_favourite_detail),
    path('purchases/<recipe_id>', api_purchase_detail),
]

urlpatterns += router.urls
