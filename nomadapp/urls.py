from django.urls import include, path
from .views import *


app_name = "nomadapp"









urlpatterns = [
    path('', post_list, name='home'),
    path('like/', like_post, name='like_post'),
    path('comments', comment_list, name='comments'),
    path('users_post/<int:user_id>', user_post_list, name='users_post'),
    path('posts/<int:post_id>', post_detail, name='post_detail'),
    # path('posts/<int:post_id>/comment/<int:post_id>', comment_detail, name='comment_detail'),
    path('posts/new', post_form, name='post_new'),
    path('posts/<int:post_id>/comment/new', add_comment, name='comment_new'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

]