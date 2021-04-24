from django import forms

from . models import Actor
from . models import Show
from . models import Genre
class Addactor_form(forms.ModelForm):
	class Meta:
		model = Actor
		fields = (
			'name',
			'image',
		)

class Addshow_form(forms.ModelForm):
	class Meta:
		model = Show
		fields = (
			'title',
			'picture',
			'release',
			'genre',
			'director',
			'rating',
			'seasons',
			'actor',
		)
