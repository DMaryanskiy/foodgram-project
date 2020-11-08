from django.db import models
from users.models import User


class Ingredients(models.Model):
    title = models.CharField(max_length=80)
    dimension = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.title, self.dimension)


class IngredientsReceipe(models.Model):
    ingredient = models.ForeignKey("Ingredients", on_delete=models.CASCADE, related_name="ingredient")
    receipe = models.ForeignKey("Receipe", on_delete=models.CASCADE, related_name="receipe", null=True, blank=True)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.ingredient.title} {self.amount} {self.ingredient.dimension}'


"""class Tag(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10)
    color = models.CharField(max_length=20)
    value = models.IntegerField(default=1)

    def __str__(self):
        return "%s" % (self.name)
"""

class Receipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="receipe/")
    descriptions = models.TextField()
    ingredient_list = models.ManyToManyField("Ingredients", through="IngredientsReceipe")
    # tag = models.ManyToManyField("Tag", related_name="tag")
    cooking_time = models.PositiveIntegerField()

    breakfast = models.BooleanField(default=False, verbose_name="Завтрак")
    lunch = models.BooleanField(default=False, verbose_name="Обед")
    dinner = models.BooleanField(default=False, verbose_name="Ужин")
