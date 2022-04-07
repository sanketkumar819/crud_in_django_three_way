from django.urls import path
from . import views
from student.models import User

urlpatterns = [
    path('',views.UserAddShowView.as_view(), name='addshow'),
    path('delete/<int:id>/',views.UserDeleteView.as_view(),name='deletedata'),
    path('update/<int:id>/',views.UserUpdateView.as_view(),name='updatedata'),
    
]
