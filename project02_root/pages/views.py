from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


from . models import Page
from . models import Show, Genre, Actor
from . forms import Addactor_form

@login_required(login_url=settings.FORCE_SCRIPT_NAME + '/accounts/login/')
def addshow_view(request, pagename='addshow'):
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	context = {
		'page_list': Page.objects.all(),
		'context': pg.bodytext, # note the end-of-line comma
	}
	return render(request, "addshow.html", context)

@login_required(login_url=settings.FORCE_SCRIPT_NAME + '/accounts/login/')
def addactor_view(request, pagename='addactor'):

	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	context = {
		'page_list': Page.objects.all(),
		'context': pg.bodytext, # note the end-of-line comma
	}
	return render(request, "addactor.html", context)

def addactor_form_submitted(request):
	submitted = False
	your_name = request.POST["your_name"]
	your_image = request.POST["your_image"]
	if request.method == 'POST':
		form = Addactor_form(request.POST)
		if form.is_valid():
			actor_info = Actor(name=your_name, image=your_image)
			actor_info.save()
			your_name = request.POST["your_name"]
			your_image = request.POST["your_image"]

			return HttpResponseRedirect(reverse('addactor') + '?submitted=True')
	else:
		form = Addactor_form()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'pages/addactor.html', context)

def index(request, pagename=''):
	pagename = '/' + pagename
	pg = Page.objects.get(permalink=pagename)
	num_actor = Actor.objects.all().count()
	num_shows = Show.objects.all().count()
	num_genres = Genre.objects.all().count()
	ac = Actor.objects.all()
	sh = Show.objects.all()
	context = {
		'num_actor': num_actor,
		'num_shows': num_shows,
		'num_genres': num_genres,
		'title': pg.title,
		'context': pg.bodytext, # note the end-of-line comma
		'last_updated': pg.update_date,
		'page_list': Page.objects.all(),
		'tv_show_list': Show.objects.all(),
		'actor_list': Actor.objects.all(),
	}
	return render(request, 'pages/page.html', context)

# Create your views here.
