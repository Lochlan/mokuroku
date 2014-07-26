# from django.shortcuts import render
from django.http import HttpResponse

from products.models import TurbografxHucard

# Create your views here.
def index(request):

    response = "<h1>HuCard Games:</h1>";
    response += "<ul>";

    for hu in TurbografxHucard.objects.all():
        response += "<li>" + hu.name + "</li>"

    response += "</ul>";

    return HttpResponse(response)
