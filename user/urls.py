from django.urls import path
from . import views
app_name ='user'
urlpatterns = [
	path('',views.index,name='index'),
	path('<int:user_id>',views.current_user,name='current_user'),
	path('new/user', views.new_user, name='new_user'),
	path('<int:user_id>/new/category', views.new_category, name='new_category')
]