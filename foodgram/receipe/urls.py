from django.urls import path

from . import views

urlpatterns = [
    path("add/ingredients", views.ingredients),
    path("", views.index, name="index"),
    path("add/receipe", views.add_receipe, name="add_receipe"),
    path("follow", views.follow_index, name="follow"),
    path("<username>", views.profile, name="profile"),
    path("<username>/follow", views.profile_follow, name="profile_follow"),
    path("<username>/unfollow", views.profile_unfollow, name="profile_unfollow"),
    path("<username>/<recipe_id>", views.recipe_view, name="recipe_view"),
]