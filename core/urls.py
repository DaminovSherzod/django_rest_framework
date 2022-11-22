from django.contrib import admin
from django.urls import path
from api.views import CreateTask, Get_Task, Get_All_Task, Remove_Task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create/', CreateTask),
    path('api/GetTask/<int:id>/', Get_Task),
    path('api/GetallTask/', Get_All_Task),
    path('api/RemoveTask/<int:id>/', Remove_Task),
]
