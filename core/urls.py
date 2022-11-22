from django.contrib import admin
from django.urls import path
from api.views import CreateTask, Get_Task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/', CreateTask),
    path('api/GetTask/<int:id>/', Get_Task),
]
