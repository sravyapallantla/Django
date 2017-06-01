from django.shortcuts import render
from rango.models import Category

from django.http import HttpResponse

def index(request):
    #return HttpResponse("Rango says hey there partner!")
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context=context_dict)

def index1(request):
    return HttpResponse("Rango says here is the about page <a href='/rango/'>Index</a>")
