from django import forms

class URLForm(forms.Form):
    original_url = forms.URLField()
