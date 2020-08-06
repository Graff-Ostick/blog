from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published__date_lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_html.html', {'posts':posts})

def show_nelka(request):
    return render(request, 'blog/nelka.html', {})