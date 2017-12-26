from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from sito.models import *
from django.core.mail import send_mail


def translation_processor(request):
	language = "it"
	session_language = "it"
	#if 'lang' in request.COOKIES:
	#	language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	context = {'language':language,
			'session_language': session_language}
	return context