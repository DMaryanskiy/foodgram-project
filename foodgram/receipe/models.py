from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingredients(models.Model):
    title = models.CharField(max_length=80)
    dimension = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.title, self.dimension)


class IngredientsRecipe(models.Model):
    ingredient = models.ForeignKey("Ingredients", on_delete=models.CASCADE, related_name="ingredient")
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="recipe", null=True, blank=True)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.ingredient.title} {self.amount} {self.ingredient.dimension}'


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="recipe/")
    descriptions = models.TextField()
    ingredient_list = models.ManyToManyField("Ingredients", related_name="recipes", through="IngredientsRecipe")
    cooking_time = models.PositiveIntegerField()

    breakfast = models.BooleanField(default=False, verbose_name="Завтрак")
    lunch = models.BooleanField(default=False, verbose_name="Обед")
    dinner = models.BooleanField(default=False, verbose_name="Ужин")


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    class Meta:
        unique_together = ['user', 'author']


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_favourite")
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="recipe_favourite")


class Purchase(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name="pur_recipe")
