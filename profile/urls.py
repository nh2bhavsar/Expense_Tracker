from django.urls import path
from .import views as core_views
from django.views.generic.base import TemplateView
from django.conf.urls import url
from django.urls import include,path
from django.contrib import admin

urlpatterns = [
	path('',core_views.home_page, name="home_page"),
    url(r'^signup/$', core_views.signup, name='signup'),
    path('accounts/profile/',core_views.home,name='home'),
    path('', include('django.contrib.auth.urls')),
    path('<str:category>',core_views.category_page,name='category_page'),
    path('new_category/',core_views.new_category,name='new_category'),
    path('new_expense/',core_views.new_expense,name='new_expense'),
    path('logout/',core_views.home, name='logout'),
    path('delete/<int:pk>/', core_views.delete_expense,name='delete_expense')
]