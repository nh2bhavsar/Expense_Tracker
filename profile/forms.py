from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Expense

class SignUpForm(UserCreationForm):
    income_per_month = forms.DecimalField()
    max_spending = forms.DecimalField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'income_per_month','max_spending', 'password1', 'password2')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'allocated_budget', 'amount_spent')

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('note', 'amount', 'category','date' )

    def __init__(self, user, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)