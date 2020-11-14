from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/recipe", views.add_recipe, name="add_recipe"),
    path("follow", views.follow_index, name="follow"),
    path("favourite", views.favourite_index, name="favourite"),
    path("purchase", views.purchase_list, name="purchase"),
    path("products", views.upload, name="get_products"),
    path("<username>", views.profile, name="profile"),
    path("<username>/<recipe_id>", views.recipe_view, name="recipe_view"),
    path("<username>/<recipe_id>/edit", views.recipe_edit, name="recipe_edit"),
    path("<username>/<recipe_id>/delete", views.recipe_delete, name="recipe_delete"),
]
