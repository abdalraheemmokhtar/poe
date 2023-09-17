from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Posts
@login_required
def index(request):
    return render(request,'core/base.html')

def contact(request):
    blog_posts = Posts.objects.all()
    return render(request,'core/contact.html',{'blog_posts':blog_posts})