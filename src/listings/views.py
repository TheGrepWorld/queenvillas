from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect , HttpResponse


def listing_page(request):
    return render(request, 'listing_page.html')


def listing_detail(request, slug):
    return HttpResponse(f'this is listing detail {slug}')