from nomadapp.models import Post
from django.shortcuts import render, redirect, reverse

def get_post(post_id):

    return Post.objects.get(pk=post_id)




def delete_post(request, post_id):
    if request.method == "GET":
        form_data = request.GET
        post = post = Post.objects.get(pk=post_id)
        context = {'post' : post}

        return render(request, context)

    if request.method == "POST":
        form_data = request.POST
        if ("actual_method" in form_data and form_data['actual_method'] == "DELETE"):
                form_data = request.POST
                print(request.POST, "here")
                post = Post.objects.get(pk=post_id)
                print(post, "PLEADE")
                post.delete()
        
        
    return redirect(reverse('nomadapp:home'))