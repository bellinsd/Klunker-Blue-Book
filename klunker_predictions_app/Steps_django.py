#mkdir

#start
django-admin startproject mysite

#cd mysite
python manage.py runserver

#Check status of server
127.0.0.1:8000


python manage.py startapp "name"

#URl / Model / Views Paradigm


#under Mysite>urls add include ('webapp')

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', include('webapp.urls')),
]

#Jinja - dynamic and logical html

from django.shortcuts import render

def index(request):
    return render(request, 'kbb_app/home.html')


Include vs Extends

"""Templates    add another file for the app templates>kbb_app
header.html
home.html


Consider Using a CDN - Bootstrap
