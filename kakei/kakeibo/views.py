from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Expense

#render関数版( loader や HttpResponse を import する必要がなくなる)
def index(request):
    latest_expense_list = Expense.objects.order_by('-expense_date')[:5]
    context = {'latest_expense_list' : latest_expense_list}
    #renderfunction in request, templateload, context
    return render(request, 'kakeibo/index.html', context)

#not renderfunction
#def index(request):
#    latest_expense_list = Expense.objects.order_by('-expense_date')[:5]
#    template = loader.get_template('kakeibo/index.html')
#    context = {'latest_expense_list' : latest_expense_list,}
#    return HttpResponse(template.render(context,request))

def detail(request, expense_id):
    return HttpResponse("you looking expense %s" % expense_id)    

def results(request, expense_id):
    response = "you looking results %s"
    return HttpResponse(response % expense_id)

def expense(rewuest, expense_id):
    return HttpResponse("you expense %s" % expense_id)
