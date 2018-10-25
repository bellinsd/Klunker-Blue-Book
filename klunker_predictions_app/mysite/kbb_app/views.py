from django.shortcuts import render

def index(request):
    return render(request, 'kbb_app/home.html')


# Create your views here.
