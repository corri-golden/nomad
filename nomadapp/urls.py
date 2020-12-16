from django.urls import include, path
from .views import *


app_name = "nomadapp"









urlpatterns = [
    path('', post_list, name='home'),
    path('posts/<int:post_id>', post_detail, name='post_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),

]