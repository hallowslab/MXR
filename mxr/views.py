from django.shortcuts import render

def index(request):
    return render(request, "mxr_index.html")
