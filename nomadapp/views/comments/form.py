from nomadapp.models import Post, Comment
from django.shortcuts import render



def comment_form(request):
    if request.method == 'GET':
        template = 'comments/form.html'

        return render(request, template)