from django.urls import path, include
from .views import index, signup_view, register_view, logout_view

urlpatterns = [
    path('', index, name='home'),  
    path('logout/', logout_view, name='logout'), 
    path('signup/', signup_view, name='signup')
]
