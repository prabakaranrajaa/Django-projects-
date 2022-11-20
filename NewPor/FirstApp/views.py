from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    mes = "<h1>hai prabakaran</h1>"
    return HttpResponse(mes)

