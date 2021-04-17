from django.shortcuts import render
from django.http import HttpResponse
from . models import Page

def index(request, pagename=''):
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	return HttpResponse(pg.bodytext)

# Create your views here.
