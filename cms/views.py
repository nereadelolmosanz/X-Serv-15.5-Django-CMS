from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages


# Create your views here.

def main_page(request):
    response = '<h1>Ejercicio 15.5: Django-CMS</h1>'
    response += '<h3>Saved pages:</h3>'
    response += '<ul>'
    pages_list = Pages.objects.all()
    for page in pages_list:
        response += '<li>' + str(page) + '</li>'
    response += '</ul>'
    return HttpResponse(response)


def page_searching(request, resource):
    try:
        pageSearched = Pages.objects.get(name=resource)
        return HttpResponse(pageSearched.page)

    except Pages.DoesNotExist:
        return HttpResponseNotFound('<h1>' + resource + ' not found.</h1>')
