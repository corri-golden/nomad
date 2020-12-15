from django.urls import include, path
from .views import *

app_name = "nomadapp"









urlpatterns = [
    path('', post_list, name='home'),
]