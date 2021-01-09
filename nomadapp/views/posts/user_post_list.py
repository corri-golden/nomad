from nomadapp.models import Post
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, reverse


# def user_post_list(request):
#     if request.method == 'GET':
#         users_post = Post.objects.filter(user_id=request.user.id)
#         # parent_pawpal_list = list(ParentPawPal.objects.filter(parent_id=parent.id))
#         user = request.user
#         template = 'posts/user_post_list.html'
#         context = {
#         'users_post': users_post,
#         'user': user,
#         }
#         return render(request, template, context)

# def get_posts():
#     all_posts = Post.objects.all()
#     return all_posts

def get_user(user_id):

    return User.objects.get(pk=user_id)


def user_post_list(request, user_id):
    if request.method == 'GET':
        # posts = get_posts()
        user = get_user(user_id)
        users_post = Post.objects.filter(user_id=user.id)
        template = 'posts/user_post_list.html'
        context = {
        'user': user,
        'users_post': users_post
        }
        return render(request, template, context)


