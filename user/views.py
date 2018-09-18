from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import User,Category
from .forms import UserForm

def index(request):
	user_list = User.objects.all()
	context = {'user_list': user_list}
	return render(request, 'user/index.html',context)

def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'user/user_edit.html', {'form': form})
