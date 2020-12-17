from nomadapp.models import Post, Comment
from django.shortcuts import render, render, reverse, redirect





def comment_list(request):
    if request.method == 'GET':

        all_comments = Comment.objects.all()
        postid = request.GET.get('postid', None)
        template = 'comments/list.html'
        context = {
            'all_comments': all_comments,
            'post_id': postid
        }

        return render(request, template, context)