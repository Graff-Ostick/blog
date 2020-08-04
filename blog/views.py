from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_html.html', {})

def show_nelka(request):
    return render(request, 'blog/nelka.html', {})