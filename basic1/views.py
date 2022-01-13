from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("안녕 django!")

def greet(request):
    return render(request, 'basic1/greet.html')

def fruit_form(request):
    return render(request, 'basic1/fruit_form.html')

def fruit(request):
    input = request.POST.get("favorite")
    print ('input = ', input)
    return HttpResponse(f"좋아하는 과일은 {input}")