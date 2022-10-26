from django.contrib import admin
from django.urls import path
from ritmos.views import clases

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clases/', clases, name='clases')
    
]
