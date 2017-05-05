from django import forms

class AddForm(forms.Form):
    a = forms.CharField(widget=forms.Textarea)
    b = forms.CharField(widget=forms.Textarea)
