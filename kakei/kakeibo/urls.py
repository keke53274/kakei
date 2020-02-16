from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:expense_id>/', views.detail, name='detail'),
    path('create', views.create, name='create'),
    #path('<int:expense_id>/expense/', views.expense, name='expense'),
    
]