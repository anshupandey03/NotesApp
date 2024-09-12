from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Noteshomepage, name="home-idx"),
    path('addnotes/', views.addnote, name='add-note'),
    path('editnotes/<int:id>/change', views.addnote, name='edit-note'),
]