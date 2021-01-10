from nomadapp.models import Post
from django.shortcuts import render, redirect, reverse

from django.shortcuts import render
from nomadapp.forms import PostForm

def get_post(post_id):

    return Post.objects.get(pk=post_id)

def get_posts():
    # if request.method == 'GET':
    all_posts = Post.objects.all()
    return all_posts


# def post_form(request):
#     if request.method == 'GET':
#         template = 'posts/form.html'
        
#         return render(request, template)




def post_form(request):
    if request.method == 'GET':
        user = request.user
        form = PostForm(instance=user)
        user_id = request.user.id

        # if request.method == 'POST':
        #     form = PostForm(request.POST, request.FILES,instance=user)
        #     if form.is_valid():
        #         form.save()


        context = {'form': form}
        return render(request, 'posts/form.html', context)

    elif request.method == 'POST':
        form_data = request.POST
        new_post = Post.objects.create(
            title = form_data['title'],
            description = form_data['description'],
            date = form_data['date'],
            post_image = request.FILES['post_image'],
            user_id = request.user.id
        )
        
    
        return redirect(reverse('nomadapp:home'))





