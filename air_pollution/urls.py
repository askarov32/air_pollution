from django.contrib import admin
from django.urls import path
from pollution_data.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home')
]
