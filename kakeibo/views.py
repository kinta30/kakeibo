from django.shortcuts import render
from django.views.generic import ListView

from .models import Payment,PaymentCategory,Income,IncomeCategory

# Create your views here.
class PaymentList(ListView):
    model = Payment
    context_object_name ="payment"
    def get_PaymentList(self):
        return "hallo world"


class IncomeList(ListView):
    model = Income
    context_object_name ="Income"

