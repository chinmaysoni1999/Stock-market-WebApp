from django.urls import path
from . import views as quotes_views

urlpatterns = [
    path('',quotes_views.home,name='home'),
    path('about/',quotes_views.about,name='about')

]
