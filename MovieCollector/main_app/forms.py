from django import forms
from .models import Cast

class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = ['name', 'age', 'notable_films', 'years_active']
