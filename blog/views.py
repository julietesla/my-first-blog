from django.shortcuts import render
from .models import Post
from django.utils import timezone
posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
def post_list(request):     
    return render(request, 'blog/post_list.html', {"posts":posts})
