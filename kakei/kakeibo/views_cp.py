#render関数を使用しているのでHttpResponseとloaderが省略できる
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
import calendar
from kakeibo.forms import InputForm

from .models import Expense

#render関数版( loader や HttpResponse を import する必要がなくなる)
def index(request):
    d = {'selecter' : request.GET.get('selecter')}
#    if d['selecter'] is None:
#        year = datetime.date.today().year
#        month = datetime.date.today().month
#        end = calendar.monthrange(year, month)[1]
#        s_day = datetime.date(year, month, 1)
#        e_day = datetime.date(year, month, end)
#    else:
#        date_dt = datetime.datetime.strptime(d['selecter'], '%Y-%m-%d')
#        date_d = date_dt.date()
#        end = calendar.monthrange(date_d.year, date_d.month)[1]
#       s_day = datetime.date(date_d.year, date_d.month, 1)
#        e_day = datetime.date(date_d.year, date_d.month, end)
#        month = date_d

    if d['selecter'] is None:
        date_d = datetime.date.today()
    else:
        date_dt = datetime.datetime.strptime(d['selecter'], '%Y-%m-%d')
        date_d = date_dt.date()

    day_list = {'year' : date_d.year, 'month': date_d.month}
    end = calendar.monthrange(date_d.year, date_d.month)[1]
    s_day = datetime.date(date_d.year, date_d.month, 1)
    e_day = datetime.date(date_d.year, date_d.month, end)
    latest_expense_list = Expense.objects.filter(expense_date__range=(s_day, e_day))
    context = {'latest_expense_list' : latest_expense_list, 'day_list' : day_list}
    return render(request, 'kakeibo/index.html', context)
    #取り出したデータを辞書に挿入
#    context = {'latest_expense_list' : latest_expense_list, 'month' : month}
    #render函数でrequest, templateload, contextを返すことができる
#    return render(request, 'kakeibo/index.html', context)


#render関数なし
#def index(request):
#    latest_expense_list = Expense.objects.order_by('-expense_date')[:5]
#    template = loader.get_template('kakeibo/index.html')
#    context = {'latest_expense_list' : latest_expense_list,}
#    return HttpResponse(template.render(context,request))

def detail(request, expense_id):
    expense = get_object_or_404(Expense, pk = expense_id)
    return render(request, 'kakeibo/detail.html', {'expense' : expense})    


#def detail(request, expense_id):
#    return HttpResponse("you looking expense %s" % expense_id)    

def results(request, expense_id):
    response = "you looking results %s"
    return HttpResponse(response % expense_id)

def expense(rewuest, expense_id):
    return HttpResponse("you expense %s" % expense_id)
