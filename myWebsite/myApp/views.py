from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')

def contact(request):
    return render(request,'contact.html')

def why(request):
    return render(request,'why.html')

def testimonial(request):
    return render(request,'testimonial.html')