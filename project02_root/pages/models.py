from django.db import models
import datetime

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    create_date = models.DateField('First Published', default = datetime.date.today)
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title

def get_years(initial=1970):
    return [(year, year) for year in range(datetime.datetime.now().year, initial, -1)]

class Genre(models.Model):
    genre = models.CharField(max_length=200, help_text='Enter a show genre (e.g. Science Fiction)')

    def __str__(self):
        return self.genre

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Show(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre, related_name='genres', help_text='Select a genre for this show')
    actor = models.ManyToManyField(Actor, related_name='actors', help_text='Select actors starring in this show this show')
    release = models.IntegerField(blank=False, default=datetime.datetime.now().year)
    rating = models.FloatField()
    seasons = models.IntegerField()

    def display_genre(self):
        return ', '.join(genre.genre for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'

    def display_actor(self):
        return ', '.join(actor.name for actor in self.actor.all()[:3])
    display_actor.short_description = 'Actor'

    def __str__(self):
        return self.title


