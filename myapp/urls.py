from django.urls import path
from .views import group_list,add_group,update_group,group_details,delete_group

urlpatterns = [

path('home/',group_list,name='groups'),
path('create-group/',add_group,name='create-groups'),
path('update-group/<int:pk>',update_group,name='update-groups'),
path('info-group/<int:pk>',group_details,name='info-groups'),
path('delete-group/<int:pk>',delete_group,name='delete-groups'),
]
