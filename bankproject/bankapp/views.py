from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def demo(request):
#     return render(request,'index.html')

from django.http import HttpResponse



def demo(request):

    return render(request, "index.html")

# def addition(request):
#     name='India'
#     return render(request,'result.html',{'obj':name})

