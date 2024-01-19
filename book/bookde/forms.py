from .models import Books
from django import forms


class Book(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"