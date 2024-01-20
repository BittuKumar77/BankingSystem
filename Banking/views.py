from django.shortcuts import render,redirect

# Create your views here.

from .models import Customer, Transaction
from .forms import TransferForm

def home(request):
    customers = Customer.objects.all()
    return render(request, 'banking/home.html', {'customers': customers})

def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']

            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount

                sender.save()
                receiver.save()

                Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)

                return redirect('home')
            else:
                error_message = 'Insufficient funds'
    else:
        form = TransferForm()
        error_message = None

    return render(request, 'banking/transfer.html', {'form': form, 'error_message': error_message})
