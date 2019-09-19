from django.shortcuts import render

def post_feed(request):
    return render(request, 'blog/post_feed.html', {})
