from django.shortcuts import render
from nomadapp.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    if request.method == 'GET':

        all_posts = Post.objects.all()

    template = 'posts/list.html'
    context = {
        'all_post': all_posts
    }
    return render(request, template, context)