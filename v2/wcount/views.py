from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.
def home(requests):
    return HttpResponse('<h1> This is my page </h1>')
def aboutus(requests):
    return HttpResponse('<h1> I am a third year student of vasavi</h1>')
def myhobbies(requests):
    return HttpResponse('<h1> I like reading books and writing</h1>')
