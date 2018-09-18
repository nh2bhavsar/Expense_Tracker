from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=200)
	income_per_month = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
	max_spending = models.DecimalField(max_digits=12, decimal_places=2)
	amount_spent = models.DecimalField(max_digits=12,decimal_places=2,default=0.00)
	
	def __str__(self):
		return self.name

class Category(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category_name = models.CharField(max_length=200)
	allocated_budget = models.DecimalField(max_digits=12, decimal_places=2)
	amount_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
	
	def __str__(self):
		return self.category_name
