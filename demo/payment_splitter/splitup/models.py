from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    title = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_expenses')
    date_created = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, through='ExpenseParticipant', related_name='expenses')

    def __str__(self):
        return self.title

class ExpenseParticipant(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} in {self.expense.title}"

class Payment(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='payments')
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_made')
    paid_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments_received')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paid_by.username} paid {self.paid_to.username} - {self.amount}"
