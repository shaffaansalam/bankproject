
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        return redirect('newpage')



    return render(request,'login.html')

def register(request):
    if request.method=='POST':

           return redirect('login')

    return render(request, "register.html")

def newpage(request):

        return render(request,'newpage.html')


def form(request):

    return render(request, 'form.html')

def logout(request):


    return render(request,'/')