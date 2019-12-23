#render関数を使用しているのでHttpResponseとloaderが省略できる
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
import datetime

from .models import Expense

#render関数版( loader や HttpResponse を import する必要がなくなる)
def index(request):
    month = datetime.date.today().month
    #DBの最新ﾃﾞｰﾀを5つ取り出す
    latest_expense_list = Expense.objects.order_by('-expense_date')[:5]
    #取り出したデータを辞書に挿入
    context = {'latest_expense_list' : latest_expense_list, 'month' : month}
    #render函数でrequest, templateload, contextを返すことができる
    return render(request, 'kakeibo/index.html', context)


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
