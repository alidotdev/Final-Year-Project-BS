from django.contrib import admin
from django.urls import path, include
from todo_api import urls as todo_urls
from . import views

urlpatterns = [
    path("", views.home),
    path("add", views.add)
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('todos/', include(todo_urls)),
]