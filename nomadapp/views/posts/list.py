from django.shortcuts import render, redirect, reverse
from nomadapp.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    if request.method == 'GET':

        all_posts = Post.objects.all()
        user = request.user
        template = 'posts/list.html'
        context = {
        'all_posts': all_posts,
        'user': user,
        }
        return render(request, template, context)

    # elif request.method == 'POST':
    #     form_data = request.POST
    #     new_post = Post.objects.create(
    #         title = form_data['title'],
    #         description = form_data['description'],
    #         location = form_data['location'],
    #         date = form_data['date'],
    #         post_image = form_data['post_image'],
    #         user_id = request.user.id
    #     )

    #     return redirect(reverse('nomadapp:home'))

