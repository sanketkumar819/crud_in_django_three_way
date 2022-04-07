from django.urls import path
from . import views
from student.models import User

urlpatterns = [
    path('',views.add_show, name='addshow'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('update/<int:id>/',views.update_data,name='updatedata'),
    
]
