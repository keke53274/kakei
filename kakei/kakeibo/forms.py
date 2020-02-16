from django import forms
from .models import Expense

class ExpenseAdd(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["expense_user", "expense", "expense_date", "expense_time", "expense_detail"]

