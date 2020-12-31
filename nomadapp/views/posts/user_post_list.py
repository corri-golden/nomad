from nomadapp.models import Post
from django.shortcuts import render, redirect, reverse


def user_post_list(request):
    if request.method == 'GET':
        users_post = Post.objects.filter(user_id=request.user.id)
        # parent_pawpal_list = list(ParentPawPal.objects.filter(parent_id=parent.id))
        user = request.user
        template = 'posts/user_post_list.html'
        context = {
        'users_post': users_post,
        'user': user,
        }
        return render(request, template, context)
