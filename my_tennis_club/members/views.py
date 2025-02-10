from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader


# def members(request):
#    return HttpResponse("Olá Mundo 10/02/2025!")

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())