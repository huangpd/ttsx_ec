from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, response

# Create your views here.
def index(request):
    return render(request,'tt_goods/index.html')