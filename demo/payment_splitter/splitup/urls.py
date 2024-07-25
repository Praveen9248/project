from django.urls import path
from . import views

urlpatterns = [
    path('create_expense/', views.create_expense, name='create_expense'),
    path('expense/<int:expense_id>/', views.expense_detail, name='expense_detail'),
    path('expense/<int:expense_id>/add_participant/', views.add_participant, name='add_participant'),
    path('expense/<int:expense_id>/record_payment/', views.record_payment, name='record_payment'),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('profile/', views.profile, name='profile'),
]
