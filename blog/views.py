from django.shortcuts import render
from django.http import HttpResponse
from . models import Post, Topic
from django.utils import timezone
from django.db.models import Count

# Create your views here.
def home(request):
    """
    The Blog homepage
    """
#     latest_posts = models.Post.objects.published().order_by('-published')[:2]
#     context = {'latest_posts': latest_posts}
    return render(request, 'blog/home.html')

def post_lists(request):
    posts = Post.objects.all().order_by('-published')  # Order by publication date in descending order
    return render(request, 'blog/post_lists.html', {'posts': posts})

def sidebar_topics(request):
    topics = Topic.objects.annotate(Count('post')).order_by('-post_count')[:10]
    return render(request, 'blog/base.html', {'topics': topics})


