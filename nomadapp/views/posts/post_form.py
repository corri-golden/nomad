from nomadapp.models import Post
from django.shortcuts import render



def post_form(request):
    if request.method == 'GET':
        template = 'posts/form.html'
        
        return render(request, template)