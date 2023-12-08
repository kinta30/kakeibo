from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView,DeleteView,UpdateView

from django.urls import reverse_lazy,reverse
from .models import Payment,PaymentCategory,Income,IncomeCategory
from datetime import datetime
# from .forms import IncomeCreate
 
# Create your views here.
class PaymentList(ListView):
    model = Payment
    context_object_name ="payments"
    
    def get_PaymentList(self):
        return "hallo world"
    def get_queryset(self):
        year = self.request.GET.get('year')
        month = self.request.GET.get('month')
        price = self.request.GET.get('price')
        category = self.request.GET.get('category')
        summary = self.request.GET.get('summary')
        # print(query+query2+query3)
        date = "2023-11"
        category = "光熱費"
        price = 1111
        if year != None and month != None:
            date=year+'-'+month
        print(date)
        print(category)
        print(price)

        if date:
            payment_list = Payment.objects.filter(
            date__icontains=date,price__icontains=price,category__name__icontains=category)
        else:
            payment_list = Payment.objects.all()
        return payment_list

class IncomeList(ListView):
    model = Income
    context_object_name ="incomes"
    def get_IncomeList(self):
        return "hallo world"

class PaymentCreate(CreateView):
    model = Payment
    context_object_name ="payment"
    fields = '__all__'
    success_url = reverse_lazy("payment_list")

class IncomeCreate(CreateView):
    model = Income
    context_object_name ="income"
    fields = '__all__'
    success_url = reverse_lazy("income_list")

class PaymentDelete(DeleteView):
    model = Payment
    context_object_name ="payment"
    success_url = reverse_lazy("payment_list")

class IncomeDelete(DeleteView):
    model = Payment
    context_object_name ="income"
    success_url = reverse_lazy("income_list")

class PaymentUpdate(UpdateView):
    model = Payment
    context_object_name ="payment"
    fields = '__all__'
    success_url = reverse_lazy("payment_list")

class IncomeUpdate(UpdateView):
    model = Payment
    context_object_name ="income"
    fields = '__all__'
    success_url = reverse_lazy("income_list")

class MonthlyPayment(TemplateView):
    model = Payment
    template_name = "Monthly_Payment.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.now()
        context['year'] = current_date.year
        context['month'] = current_date.month
        context['monthly_payment_url'] = reverse('Monthly_Payment', kwargs={'year': context['year'], 'month': context['month']})
        return context

class transition(TemplateView):
    model = Payment
    template_name = "transition"