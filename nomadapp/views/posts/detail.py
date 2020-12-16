from nomadapp.models import Post
from django.shortcuts import render


def get_post(post_id):

    return Post.objects.get(pk=post_id)



def post_detail(request, post_id):
    if request.method == 'GET':
        post = get_post(post_id)
        template_name = 'posts/detail.html'
        print("post: ", post)
        return render(request, template_name, {'post': post})
