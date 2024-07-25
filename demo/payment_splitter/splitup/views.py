
from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense, ExpenseParticipant, Payment
from .forms import ExpenseForm, ExpenseParticipantForm, PaymentForm
from django.contrib.auth.decorators import login_required

@login_required
def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.created_by = request.user
            expense.save()
            return redirect('expense_detail', expense.id)
    else:
        form = ExpenseForm()
    return render(request, 'splitup/create_expense.html', {'form': form})

@login_required
def expense_detail(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    participants = ExpenseParticipant.objects.filter(expense=expense)
    payments = Payment.objects.filter(expense=expense)
    return render(request, 'splitup/expense_detail.html', {
        'expense': expense, 'participants': participants, 'payments': payments
    })

@login_required
def add_participant(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        form = ExpenseParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.expense = expense
            participant.save()
            return redirect('expense_detail', expense.id)
    else:
        form = ExpenseParticipantForm()
    return render(request, 'splitup/add_participant.html', {'form': form, 'expense': expense})

@login_required
def record_payment(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.expense = expense
            payment.save()
            return redirect('expense_detail', expense.id)
    else:
        form = PaymentForm()
    return render(request, 'splitup/record_payment.html', {'form': form, 'expense': expense})

def expense_list(request):
    expenses = Expense.objects.all()  # Fetch all expenses
    return render(request, 'splitup/expense_list.html', {'expenses': expenses})

def profile(request):
    # Render a simple profile page
    return render(request, 'splitup/profile.html')
