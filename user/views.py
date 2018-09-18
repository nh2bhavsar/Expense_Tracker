from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import User,Category
from .forms import UserForm, CategoryForm

def index(request):
	user_list = User.objects.all()
	context = {'user_list': user_list}
	return render(request, 'user/index.html',context)

def current_user(request,user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/users.html',{'user':user})

def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            add_user = form.save(commit=False)
            add_user.save()
            return redirect('user:index')
    else:
        form = UserForm()
    return render(request, 'user/user_new.html', {'form': form})

def new_category(request,user_id):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            add_cat = form.save(commit=False)
            add_cat.user=User.objects.get(pk=user_id)
            add_cat.save()
            return redirect('user:current_user',user_id)
    else:
        form = CategoryForm()
    return render(request, 'user/new_category.html', {'form': form})