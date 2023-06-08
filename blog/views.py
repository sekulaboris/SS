from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts= Post.published.all()
    return render (request,
                    'list.html',
                    {'post':post})

def post_detail(request, year, month, day, post):
    post=get_object_or_404( Post, slug=post,
                                    status='published',
                                    publish__year=yera,
                                    publish__month=month,
                                    publish__day=day,)
    return render (request, 
                    'detail.html',
                    {'post':post})

# Create your views here.
