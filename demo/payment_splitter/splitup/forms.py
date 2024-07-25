from django import forms
from .models import Expense, ExpenseParticipant, Payment

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'total_amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_amount'].widget.attrs.update({'class': 'form-control'})

class ExpenseParticipantForm(forms.ModelForm):
    class Meta:
        model = ExpenseParticipant
        fields = ['user', 'amount_due']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount_due'].widget.attrs.update({'class': 'form-control'})

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['paid_by', 'paid_to', 'amount']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['paid_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['paid_to'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
