from nomadapp.models import Post, Comment
from django.shortcuts import render, redirect, reverse

# def get_post(post_id):
#     return Post.objects.get(pk=post_id)

# def add_comment(request, post_id):
#     if request.method == 'GET':
#         template = 'comments/form.html'
#         post = get_post(post_id)

#         context = {
#             'post': post
#         }
#         return render(request, template, context)

def add_comment(request, post_id):
    if request.method == 'GET':
        template = 'comments/form.html'

        return render(request, template)

    elif request.method == 'POST':
        form_data = request.POST
        print(form_data, 'form_data')
        post_id = Post.objects.get(id=post_id)
        new_comment = Comment.objects.create(
            message = form_data['message'],
            post_id = post_id.id,
            user_id = request.user.id
        )
        # body = form_data['message']
        # post = Post.objects.get(id=post_id)
        
        # Comment.objects.create(
        #     body=body, 
        #     post=post
        #     )

        return redirect(reverse('nomadapp:post_detail', args=[post_id.id]))