from django.db import models
from django.utils import timezone

# Create your models here.

#Expense(syuppi)
class Expense(models.Model):
    expense_user = models.CharField(max_length=200, null = True)
    expense = models.BigIntegerField(default=0)
    expense_date = models.DateTimeField('date published')
    expense_detail = models.CharField(max_length=200)
    #「Expense.objects.all()」をした時、結果の「<QuerySet [<Expense:☆☆☆ >]>」の「☆」の部分になる
    def __str__(self):
        #return self.expense_detail
        return self.expense_user

    #年月日で公開された質問を入手
    def was_published_recently(self):
        return self.expense_date >= timezone.now() - datetime.timedelta(days=1)