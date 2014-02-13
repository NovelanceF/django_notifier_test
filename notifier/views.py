from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout

def index(request):
    context = RequestContext(request, {})
    return render(request, 'notifier/index.html', context)

def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        print request.user
        context = RequestContext(request, {})
        return render(request, 'notifier/loged.html', context)
    else:
        context = RequestContext(request, {})
        return render(request, 'notifier/re_log.html', context)

def logout_view(request):
    logout(request)
    context = RequestContext(request, {})
    return render(request, 'notifier/index.html', context)
