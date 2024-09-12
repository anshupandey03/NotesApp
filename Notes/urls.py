from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.Noteshomepage, name="home-idx"),
    path('addnotes/', views.addnote, name='add-note'),
    path('editnotes/<int:id>', views.editnote, name='edit-note'),
    path('deletenotes/<int:id>', views.deletenote, name='delete-note'),
]