from django.contrib import admin

from .models import Profile,Category, Expense

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Expense)
