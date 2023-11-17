from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView

from .models import Payment,PaymentCategory,Income,IncomeCategory
# from .forms import IncomeCreate
 
# Create your views here.
class PaymentList(ListView):
    model = Payment
    context_object_name ="payments"
    def get_PaymentList(self):
        return "hallo world"


class IncomeList(ListView):
    model = Income
    context_object_name ="Income"

class PaymentCreate(CreateView):
    model = Payment
    context_object_name ="payment"
    fields = '__all__'

class IncomeCreate(CreateView):
    model = Income
    context_object_name ="Income"
    fields = '__all__'

class MonthlyPayment(TemplateView):
    model = Payment
    template_name = "Monthly_Payment.html"