from django.urls import path,include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('add', add_news)

]
