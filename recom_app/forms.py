from django import forms
import os

class TextForm(forms.Form):
    lines = []
    current_path = os.getcwd()
    with open(current_path+"/recom_app/filmler_tekil.txt", encoding="utf8") as f:
        for line in f:
            lines.append(line.strip()) 

    CHOICES= []
    for film in lines:
        CHOICES.append((film,film))

    film_selector = forms.ChoiceField(
        choices=CHOICES, 
        widget=forms.Select(attrs={'id': 'film_selector','class': 'film_selector'}))