from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	income_per_month = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=True)
	max_spending = models.DecimalField(max_digits=12, decimal_places=2,blank=True,default=0)
	amount_spent = models.DecimalField(max_digits=12,decimal_places=2,default=0,blank=True)
	def __str__(self):
		return self.user.username
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Category(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	category_name = models.CharField(max_length=200)
	allocated_budget = models.DecimalField(max_digits=12, decimal_places=2)
	amount_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
	
	def __str__(self):
		return self.category_name

class Expense(models.Model):
    note = models.CharField(max_length=30)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
    	return self.note