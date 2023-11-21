from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView,DeleteView,UpdateView

from django.urls import reverse_lazy
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
    def get_IncomeList(self):
        return "hallo world"

class PaymentCreate(CreateView):
    model = Payment
    context_object_name ="payment"
    fields = '__all__'
    success_url = reverse_lazy("payment_list")

class IncomeCreate(CreateView):
    model = Income
    context_object_name ="Income"
    fields = '__all__'
    success_url = reverse_lazy("payment_list")

class PaymentDelete(DeleteView):
    model = Payment
    context_object_name ="payment"

class PaymentUpddate(UpdateView):
    model = Payment
    context_object_name ="payment"


class MonthlyPayment(TemplateView):
    model = Payment
    template_name = "Monthly_Payment.html"

class transition(TemplateView):
    model = Payment
    template_name = "transition"