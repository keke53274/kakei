from django.contrib import admin
from .models import Expense
# Register your models here.

#adminﾍﾟｰｼﾞを開いた際にkakeiboｱﾌﾟﾘが表示されるようにadminに伝える
admin.site.register(Expense)
