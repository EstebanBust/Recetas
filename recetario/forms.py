# En tu archivo forms.py
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'description', 'instructions', 'created_by', 'image1', 'image2', 'image3']
