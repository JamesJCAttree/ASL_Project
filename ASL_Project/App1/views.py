from django.shortcuts import render, redirect

# Create your views here.

#Loads the main page for the translator
def MainPage (request):
    return render(request, "app1/MainPage.html")
