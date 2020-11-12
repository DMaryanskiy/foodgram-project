from django.urls import path

from . import views

urlpatterns = [
    path("add/ingredients", views.ingredients),
    path("", views.index, name="index"),
    path("add/receipe", views.add_receipe, name="add_receipe"),
    path("follow", views.follow_index, name="follow"),
    path("favourite", views.favourite_index, name="favourite"),
    path("<username>", views.profile, name="profile"),
    path("<username>/<recipe_id>", views.recipe_view, name="recipe_view"),
    path("<username>/<recipe_id>/edit", views.recipe_edit, name="recipe_edit"),
    path("<username>/<recipe_id>/delete", views.recipe_delete, name="recipe_delete"),
]