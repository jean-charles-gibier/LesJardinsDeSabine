from django.shortcuts import render

from django.http import HttpResponse

# la vue la "plus simple possible"
def index(request):
    return HttpResponse("Hello, world. You're at the website of 'Les Jardins de Sabine' index.")