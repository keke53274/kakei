def index(request):
    if request.method == 'POST':
        d = {'selecter' : request.POST.get('selecter')}
        date_dt = datetime.datetime.strptime(d['selecter'], '%Y-%m-%d')
        date_d = date_dt.date()
    else:
        date_d = datetime.date.today()

    #対象年月検索用変数
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