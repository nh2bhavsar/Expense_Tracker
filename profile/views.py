from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, CategoryForm, ExpenseForm
from .models import Profile, Category, Expense
from datetime import datetime

def home_page(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.income_per_month = form.cleaned_data.get('income_per_month')
            user.profile.max_spending= form.cleaned_data.get('max_spending')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home_page')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    user=request.user
    profile = user.profile
    current_month=datetime.now().month
    return render(request, 'home.html',{'profile':profile,'current_month':current_month})

def category_page(request,category):
    category= Category.objects.get(category_name__iexact=category)
    return render(request, 'category.html',{'category':category})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            add_cat = form.save(commit=False)
            add_cat.user=(request.user).profile
            add_cat.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'new_category.html', {'form': form})

def new_expense(request):
    if request.method == 'POST':
        form = ExpenseForm((request.user).profile, request.POST)
        if form.is_valid():
            user=request.user
            profile=user.profile
            expense = form.save(commit=False)
            expense.user = user
            profile.amount_spent+=form.cleaned_data.get('amount')
            profile.save()
            expense.save()
            category= expense.category
            category.amount_spent+=expense.amount
            category.save()
            return redirect('home')
    else:
        form = ExpenseForm((request.user).profile)
    return render(request, 'new_expense.html', {'form': form})
