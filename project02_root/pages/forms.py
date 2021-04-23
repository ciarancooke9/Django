from django import forms

class Addactor_form(forms.Form):
	your_name = forms.CharField(max_length=100, label='Your name')
	your_image = forms.ImageField()