from django.urls import path
from.import views



urlpatterns=[
    path('',views.index,name='index'),


  #  path('static/Mumbai/',views.Mumbai,name='Mumbai'),
   # path('static/Hyderabad/',views.Hyderabad,name='Hyderabad'),
  #  path('static/Pune/',views.Pune,name='Pune'),
   # path('static/Bangalore/',views.Bangalore,name='Bangalore'),
  #  path('static/Delhi/',views.Delhi,name='Delhi')

]

