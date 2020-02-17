from django import forms
from .models import Expense
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ExpenseAdd(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        #fields = ["expense_user", "expense", "expense_date", "expense_time", "expense_detail"]
        widgets = {
            #"expense_date" : AdminDateWidget(),
            'expense_date' : DateInput(),
            'expense_time' : TimeInput(),
        }


