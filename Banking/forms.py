from django import forms

from .models import Customer

class TransferForm(forms.Form):
    sender = forms.ModelChoiceField(queryset=Customer.objects.all())
    receiver = forms.ModelChoiceField(queryset=Customer.objects.all())
    amount = forms.DecimalField()