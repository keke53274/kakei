from django.db import models

# Create your models here.

#Expense(syuppi)
class Expense(models.Model):
    expense_user = models.CharField(max_length=200, null = True)
    expense = models.BigIntegerField(default=0)
    expense_date = models.DateTimeField('date published')
    expense_detail = models.CharField(max_length=200)