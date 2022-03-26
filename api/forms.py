from django import forms

class GalleryForm(forms.Form):
    at_home = forms.BooleanField()

