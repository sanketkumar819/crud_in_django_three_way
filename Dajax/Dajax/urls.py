from django.contrib import admin
from django.urls import path, include
from Djcrudfun import urls
from Djcrudclass import urls
from student import urls
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.common,name='common'),
    path('fbv/',include('Djcrudfun.urls')),
    path('cbv/',include('Djcrudclass.urls')),
    path('ajax/',include('student.urls')),
    
    
]
