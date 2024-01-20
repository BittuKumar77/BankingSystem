from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

