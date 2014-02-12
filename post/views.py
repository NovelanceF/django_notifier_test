from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from post.models import Post

def post_index(request):
    post_list = Post.objects.order_by('-post_date')[:10]
    context = RequestContext(request, {
        'post_list': post_list
    })
    return render(request, 'post/index.html', context)

def post_save(request):
    if request.POST.has_key('post_dog'):
        post_dog = request.POST['post_dog']
        date = request.POST['post_date']
        post_body = request.POST['post_body']
        p = Post(dog = post_dog, post_date = date, body = post_body)
        p.save()

        post_list = Post.objects.order_by('-post_date')[:10]
        context = RequestContext(request, {
            'post_list': post_list
        })
        return render(request, 'post/index.html', context)

    else:
        return
