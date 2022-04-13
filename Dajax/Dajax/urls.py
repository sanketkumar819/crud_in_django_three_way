from django.contrib import admin
from django.urls import path, include
from Djcrudfun import views
from Djcrudclass import views
from student import views
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.common,name='common'),
    path('fbv/',include('Djcrudfun.urls')),
    path('cbv/',include('Djcrudclass.urls')),
    path('ajax/',include('student.urls')),
    path('api/', include('student.api.urls')),
    
    
]
