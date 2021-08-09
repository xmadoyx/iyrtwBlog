from django.shortcuts import render
from django.shortcuts import HttpResponse
# HttpResponse takes HttpRequest and shows the value that we want to the user

def about(request):
    # return HttpResponse('if youre reading this, Wait... heres a place to... ponder! :)')
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('If You're Reading This... Wait')
    return render(request, 'home.html')
