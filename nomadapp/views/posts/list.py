from django.shortcuts import render, redirect, reverse
from nomadapp.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#used so we can search by two parameters
from django.db.models import Q

# Create your views here.

def get_users():
    all_users = User.objects.all()
    return all_users




def post_list(request):
    if request.method == 'GET':

    #for the search functionality
        #get the data from the search bar through the get.  comes as a dictionary
        #added name in the search form and the value of user will become key in the dict. of request object
        search_query = request.GET.get('search', '')
        print(search_query)
        #if search_query is = to titles then filter only the titles and description.
        if search_query:
            all_posts = Post.objects.filter(Q(title__icontains=search_query) |
            Q(description__icontains=search_query) | Q(user__username__icontains=search_query))
        else:
            all_posts = Post.objects.all().order_by('-date')
    user = request.user
    users = get_users()
    template = 'posts/list.html'
    context = {
    'all_posts': all_posts,
    'users': users,
    'user': user,
    }
    return render(request, template, context)

  

