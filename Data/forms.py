from django import forms

from .models import search

class serachform(forms.ModelForm):
    class Meta:
        model = search
        fields=[
            'search'
        ]


