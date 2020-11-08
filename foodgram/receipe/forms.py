from django import forms

from .models import Receipe


class ReceipeForm(forms.ModelForm):
    class Meta:
        model = Receipe
        fields = ["title", "breakfast", "lunch", "dinner", "cooking_time", "descriptions", "image", ]
        widgets = {
            "tag" : forms.CheckboxSelectMultiple(),
        }
