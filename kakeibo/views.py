from django.shortcuts import render
from django.views.generic import ListView,CreateView,TemplateView,DeleteView,UpdateView

from django.urls import reverse_lazy,reverse
from .models import Payment,PaymentCategory,Income,IncomeCategory
# from .forms import IncomeCreate
 
# Create your views here.
class PaymentList(ListView):
    model = Payment
    context_object_name ="payments"
    
    def get_PaymentList(self):
        return "hallo world"
    def get_queryset(self):
        query = self.request.GET.get('year')
        query4 = self.request.GET.get('month')
        query2 = self.request.GET.get('category')
        query3 = self.request.GET.get('summary')
        # print(query+query2+query3)
        date = "2023-11"
        query2 = "光熱費"
        if query != None and query4 != None:
            date=query+'-'+query4
        print(date)


        if query:
            payment_list = Payment.objects.filter(
                date__icontains=date,category=query2)
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
        context['year'] = 2023
        context['month'] = 11
        context['monthly_payment_url'] = reverse('Monthly_Payment', kwargs={'year': context['year'], 'month': context['month']})
        return context

class transition(TemplateView):
    model = Payment
    template_name = "transition"