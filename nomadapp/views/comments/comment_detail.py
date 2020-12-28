# from nomadapp.models import Post, Comment
# from django.shortcuts import render


# def get_post(post_id):

#     return Post.objects.get(pk=post_id)


# def comment_detail(request, comment_id):
#     if request.method == 'GET':
#         post = get_post(post_id)
#         comments = get_comments(comment_id)
#         template_name = 'comments/detail.html'
#         context = {
#             'all_comments': comments,
#             'all_posts': posts
#         }
#         print("post: ", post)
#         return render(request, template_name, {'post': post})