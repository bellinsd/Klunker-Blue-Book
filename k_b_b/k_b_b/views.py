from django.shortcuts import render

def index(request):
    return render(request, 'k_b_b/home.html')
