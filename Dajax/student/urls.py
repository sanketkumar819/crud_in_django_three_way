from django.urls import path
from student import views

urlpatterns = [
    
    path('',views.home,name='index'),
    path('savedata/',views.save_data,name='save'),
    path('deletedata/',views.delete_data,name='delete'),
    path('editdata/',views.edit_data,name='edit'),
    
    
]
