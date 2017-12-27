from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from sito.models import *
from django.core.mail import send_mail
from filer.models import *

from datetime import datetime

# Create your views here

def HomePage(request):
    post_list = Post.objects.all().order_by('-id')
    slider_list = Post.objects.all().order_by('pub_date')
    news_list = News.objects.all().order_by('-pub_date')[:4]
    box_list = Box.objects.all()
    gioielli = Page.objects.get(id=1)
    biografia = Page.objects.get(id=2)
    slogan = Page.objects.get(id=6)
    context = {'post_list':post_list,
                'slider_list':slider_list,
                'news_list':news_list,
                'box_list':box_list,
                'gioielli':gioielli,
                'biografia':biografia,
                'slogan':slogan
    }
    # return render_to_response('index.html', context, context_instance=RequestContext(request))
    return render(request, 'index.html', locals())



def ProductView(request):
    post_list = Post.objects.all().order_by('-id')
    categorie_list = Categorie.objects.all()
    context = {'post_list':post_list,
                'categorie_list':categorie_list}
    # return render_to_response('prodotti.html', context, context_instance=RequestContext(request))
    return render(request, 'prodotti.html', locals())


def ProductFilterView(request, post_id):
    post_list = Post.objects.filter(categoria_id = post_id).order_by('-id')
    categorie_list = Categorie.objects.all()
    context = {'post_list':post_list,
                'categorie_list':categorie_list}
    # return render_to_response('prodotti.html', context, context_instance=RequestContext(request))
    return render(request, 'prodotti.html', locals())


def DetailView(request, post_id):
    post = Post.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = post.album)
    context = {'post': post,
    			'filer_list':filer_list}
    #return render_to_response('dettaglio.html', context, context_instance=RequestContext(request))
    return render(request, 'dettaglio.html', locals())


def categorie(request):
	categorie_list = Categorie.objects.all()
	context = {'categorie_list':categorie_list}
	return context


def news(request):
    tipologie_list = TipologiaEventi.objects.all()
    news_list = News.objects.all().order_by('-pub_date')
    context = {'tipologie_list':tipologie_list,
                'news_list':news_list}
    #return render_to_response('news.html', context, context_instance=RequestContext(request))
    return render(request, 'news.html', locals())

def newsFilter(request, post_id):
    tipologie_list = TipologiaEventi.objects.all()
    news_list = News.objects.filter(categoria_id=post_id).order_by('-pub_date')
    categoria = TipologiaEventi.objects.get(id=post_id)
    context = {'tipologie_list':tipologie_list,
                'news_list':news_list,
                'categoria':categoria}
    #return render_to_response('news.html', context, context_instance=RequestContext(request))
    return render(request, 'news.html', locals())


### EMAIL - CONTACT FORM
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'MESSAGGIO DAL SITO SABRIART BIJOUX'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contact.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['info@sabriartbijoux.it']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/success/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    #return render_to_response('contact.html', {'form': form,})
    # return render_to_response('contact.html', context_instance=RequestContext(request))
    return render(request, 'contact.html', locals())



### EMAIL - CONTACT FORM
def shop(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'MESSAGGIO DAL SITO SABRIART BIJOUX'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contact.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['info@sabriartbijoux.it']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/success/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    #return render_to_response('contact.html', {'form': form,})
    # return render_to_response('shop.html', context_instance=RequestContext(request))
    return render(request, 'shop.html', locals())




def success(request):
    # return render_to_response('success.html', context_instance=RequestContext(request))
    return render(request, 'success.html', locals())


### setting language session
def language(request, language='it'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
