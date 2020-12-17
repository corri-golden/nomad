from nomadapp.models import Post, Comment
from django.shortcuts import render


def get_comments():
    all_comments = Comment.objects.all()
    return all_comments

def get_post(post_id):

    return Post.objects.get(pk=post_id)



def post_detail(request, post_id):
    if request.method == 'GET':
        post = get_post(post_id)
        comments = get_comments()
        template_name = 'posts/detail.html'
        context = {
            'all_comments': comments
        }
        print("post: ", post)
        return render(request, template_name, {'post': post})
