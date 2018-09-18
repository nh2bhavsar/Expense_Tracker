from django import forms

from .models import User, Category

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'income_per_month','max_spending')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('category_name', 'allocated_budget')