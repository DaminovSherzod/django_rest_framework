from django.contrib import admin
from django.urls import path
from api.views import CreateTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/', CreateTask),
]
