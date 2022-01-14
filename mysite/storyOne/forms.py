from django import forms

class NameForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea, label='Votre code')
