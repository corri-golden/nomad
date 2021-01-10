from nomadapp.models import Post, Comment
from django.shortcuts import render, redirect, reverse


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

    elif request.method == 'POST':
        form_data = request.POST
        print(form_data, "!!!!!!!!!!!!")

    if (
        "actual_method" in form_data 
        and form_data["actual_method"] == "PUT"
        ):
        post_to_update = Post.objects.get(pk=post_id)
        print(post_to_update, "Hereeee")

        post_to_update.title = form_data['title']
        post_to_update.description = form_data['description']
        post_to_update.date = form_data['date']
        post_to_update.post_image = form_data['post_image']

        post_to_update.save()

        return redirect(reverse('nomadapp:home'))

    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
        ):

    

        post = Post.objects.get(pk=post_id)
        print(post, "HERE")
        post.delete()

        return redirect(reverse('nomadapp:home'))


