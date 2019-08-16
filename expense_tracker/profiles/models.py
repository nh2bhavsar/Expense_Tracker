# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver

class Profile(models.Model):
    BUDGET_TRACKING = (
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
        ('Q', 'QuarterTermly'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    tracking = models.CharField(max_length=1, choices=BUDGET_TRACKING,
                help_text="Which interval would you like to budget?")
    def __str__(self):
        return self.user.username

@receiver (models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

class Income(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    source = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Expense(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class BudgetInterval(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    starting_date = models.DateField()
    ending_date = models.DateField()
