from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def amp(request):
    return render(request,'index.amp.html')

def feed(request):
    return render(request,'feed.html')
