from django.db import models
from users.models import User


class Ingredients(models.Model):
    title = models.CharField(max_length=80)
    dimension = models.CharField(max_length=10)


class IngredientsReceipe(models.Model):
    ingredient = models.ForeignKey("Ingredients", on_delete=models.CASCADE, related_name="ingredient")
    amount = models.IntegerField()


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.name)


class Receipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="receipe/")
    descriptions = models.TextField()
    ingredient_list = models.ForeignKey("IngredientsReceipe", on_delete=models.CASCADE, related_name="receipe")
    tag = models.ManyToManyField("Tag", related_name="tag")
    cooking_time = models.IntegerField()
