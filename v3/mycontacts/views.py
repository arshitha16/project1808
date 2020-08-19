from django.shortcuts import render
from django.http import HttpResponse
import operator
def mail(requests):
    return HttpResponse('My work email id is arshitha@gmail.com')
def number(requests):
    return HttpResponse('You can contact me at 9876543210')
# Create your views here.
