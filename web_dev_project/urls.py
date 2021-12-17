from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('massively.urls')),
    path('admin/', admin.site.urls),
]
