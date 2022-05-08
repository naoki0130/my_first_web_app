from tkinter import Label
from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True,
    )