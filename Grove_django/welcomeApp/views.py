from django.http import HttpResponse
from django.shortcuts import render

def initPage(request):
    return render(request, "index.html")
    return HttpResponse("Knowing about the almost mythic street racing team known as the “Mid Night Club” is essential knowledge for any fan of the Japanese street racing scene or the late 80s and 90s Japanese car culture that was bustling at the time.")

def aboutPage(reguest):
    return HttpResponse("About us")