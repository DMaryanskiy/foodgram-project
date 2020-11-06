from django.urls import path

from . import views

urlpatterns = [
    path("add/ingredients", views.ingredients)
]