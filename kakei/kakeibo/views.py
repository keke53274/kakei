from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
import calendar
from .forms import ExpenseAdd
from .models import Expense
from django.shortcuts import redirect

#forms.py not use
#POSTの場合は「memo.py」に記載
def index(request):
    #index.htmlから入力された年月selecterをdに格納して処理
    d = {'selecter' : request.GET.get('selecter')}
    if d['selecter'] is None:
        #初期表示の場合
        date_d = datetime.date.today()
    else:
        #年月を入力された場合
        date_dt = datetime.datetime.strptime(d['selecter'], '%Y-%m')
        date_d = date_dt.date()

    #対象年月検索用
    day_list = {'year' : date_d.year, 'month': date_d.month}
    end = calendar.monthrange(date_d.year, date_d.month)[1]
    s_day = datetime.date(date_d.year, date_d.month, 1)
    e_day = datetime.date(date_d.year, date_d.month, end)

    #対象抽出
    latest_expense_list = Expense.objects.filter(expense_date__range=(s_day, e_day))
    #合計金額
    full = 0
    for e in latest_expense_list:
        full += e.expense

    #取り出したデータを辞書に挿入
    context = {'latest_expense_list' : latest_expense_list, 'day_list' : day_list, 'full': full}
    #render函数でrequest, templateload, contextを返すことができる
    return render(request, 'kakeibo/index.html', context)

def detail(request, expense_id):
    expense = get_object_or_404(Expense, pk = expense_id)
    return render(request, 'kakeibo/detail.html', {'expense' : expense})


def create(request):
    if (request.method == "POST"):
        obj = Expense()
        add = ExpenseAdd(request.POST, instance=obj)
        add.save()
        return redirect(to='index')
    modelform_dict = {
        'title':'新規',
        'form':ExpenseAdd,
        }
    return render(request, 'kakeibo/create.html', modelform_dict)


#def detail(request, expense_id):
#    return HttpResponse("you looking expense %s" % expense_id)    
"""
未
def results(request, expense_id):
    response = "you looking results %s"
    return HttpResponse(response % expense_id)

def expense(rewuest, expense_id):
    return HttpResponse("you expense %s" % expense_id)
"""