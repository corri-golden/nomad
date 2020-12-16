from django.urls import include, path
from .views import *


app_name = "nomadapp"









urlpatterns = [
    path('', post_list, name='home'),
    path('posts/<int:post_id>', post_detail, name='post_detail'),
    path('posts/new', post_form, name='post_new'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

]