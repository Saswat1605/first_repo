from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_name(reqquest):
    return HttpResponse('<marquee><h1>you cant see me<h1><marquee/>')