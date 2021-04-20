from django.shortcuts import render
from django.http import HttpResponse
from . models import Page
from . models import Show, Genre, Actor

def index(request, pagename=''):
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	context = {
		'title': pg.title,
		'context': pg.bodytext, # note the end-of-line comma
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
		'tv_show_list': Show.objects.all(),
	}
	return render(request, 'pages/page.html', context)

# Create your views here.
