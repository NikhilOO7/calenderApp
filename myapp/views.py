from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.

# def index(request):
# 	return HttpResponse("It works!");

def index(request):
	entries = Entry.objects.all()
	return render(request, 'myapp/index.html', {'entries' : entries})

def details(request, pk):
	entry = Entry.objects.get(id=pk)
	return render(request, 'myapp/details.html', {'entry' : entry})