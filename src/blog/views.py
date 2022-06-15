from ast import Try
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from blog.models import BlogPost

# Create your views here.
def blogPost(request):
    return redirect("https://docs.djangoproject.com/fr/4.0/topics/http/shortcuts/#render")
    
    
