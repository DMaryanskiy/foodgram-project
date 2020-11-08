from django.urls import path

from . import views

urlpatterns = [
    path("add/ingredients", views.ingredients),
    path("", views.index, name="index"),
    path("add/receipe", views.add_receipe, name="add_receipe"),
    # path("<username>", views.profile, name="profile")
]