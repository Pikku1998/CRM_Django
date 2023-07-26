from django.urls import path, include
from .views import index, signup_view, register_view, logout_view, view_record, add_record

urlpatterns = [
    path('', index, name='home'),  
    path('logout/', logout_view, name='logout'), 
    path('signup/', signup_view, name='signup'),
    path('record/<int:pk>', view_record, name='view_record'),
    path('add_record/', add_record, name='add_record'),

]
