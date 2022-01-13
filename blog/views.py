from django.shortcuts import render

# Create your views here.
from .models import Post
from django.shortcuts import redirect


def view_blog_list(request):
    # blog_list = Post.objects.all()
    blog_list = Post.objects.order_by('-created_at')
    data = {'post_list': blog_list}
    return render(request, 'blog/view_blog_list.html', data)

def view_blog(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    data = {'blog': blog}
    return render(request, 'blog/view_blog.html', data)

def add_blog_form(request):
    return render(request, 'blog/add_blog_form.html')

def add_blog(request):
    input1 = request.POST.get('title')
    input2 = request.POST.get('writer')
    input3 = request.POST.get('content')
    p = Post(title = input1, writer = input2, content = input3)
    p.save()
    return redirect('/')

def edit_blog_form(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    data = {'blog': blog}
    return render(request, 'blog/edit_blog_form.html', data)

def edit_blog(request):
    input1 = request.POST.get('title')
    input3 = request.POST.get('content')
    input4 = request.POST.get('id')

    b = Post.objects.get(id = input4)
    b.title = input1
    b.content = input3
    b.save()
    link = 'http://127.0.0.1:8000/blog/view_blog/'+str(input4)
    return redirect(link)

def delete_blog(request, blog_id):
    blog = Post.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')