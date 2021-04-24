from django import forms

from . models import Actor
from . models import Show

class Addactor_form(forms.ModelForm):
	class Meta:
		model = Actor
		fields = (
			'name',
			'image',
		)
