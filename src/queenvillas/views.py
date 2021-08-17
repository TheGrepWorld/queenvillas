from django.shortcuts import render, redirect
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home_page.html')
