from django.urls import path, include
from .views import index,register_view, logout_view

urlpatterns = [
    path('', index, name='home'),  
    path('logout/', logout_view, name='logout'), 
    path('register/', register_view, name='register')
]
