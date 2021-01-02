from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    context["title"] = "Main"

    return render(request, "home.html", context)