from django.db.models import Sum
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
        price = 55555
        print(year)
        print(month)
        if year != None and month != None:
            print('C')
            date=year+'-'+month
        print(date)
        print(category)
        print(price)
        sum=0
        filters = {}
        print('B')

        payment_list = {}
        if date:
            filters['date__icontains'] = date
            print('A')
            print( filters['date__icontains'])
        if category:
            filters['category__name__icontains'] = category
            print( filters['category__name__icontains'])
        if summary:
            filters['summary__icontains'] = summary
            print( filters['summary__icontains'])

        if filters:
            payment_list = Payment.objects.filter(**filters)
            return payment_list
        else :
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_year = datetime.now().year
        current_date = datetime.now()
        context['years'] = range(2020, current_year + 1)
        context['months'] = range(1, 13)
        context['current_year'] = current_date.year
        context['current_month'] = current_date.month
        context['search_form'] = {
        'year': self.request.GET.get('year'),
        'month': self.request.GET.get('month'),
        'category': self.request.GET.get('category'),
        'summary': self.request.GET.get('summary'),
        }

        return context


class IncomeList(ListView):
    model = Income
    context_object_name ="incomes"
    def get_IncomeList(self):
        return "hallo world"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.now()
        context['current_year'] = current_date.year
        context['current_month'] = current_date.month
        return context

class PaymentCreate(CreateView):
    model = Payment
    context_object_name ="payment"
    fields = '__all__'
    success_url = reverse_lazy("payment_list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.now()
        context['current_year'] = current_date.year
        context['current_month'] = current_date.month
        return context

class IncomeCreate(CreateView):
    model = Income
    context_object_name ="income"
    fields = '__all__'
    success_url = reverse_lazy("income_list")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.now()
        context['current_year'] = current_date.year
        context['current_month'] = current_date.month
        return context

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
        context['prevyear'] = current_date.year
        context['prevmonth'] = current_date.month-1
        context['year'] = current_date.year
        context['month'] = current_date.month
        context['nextyear'] = current_date.year
        if current_date.month == 12:
            context['nextyear'] +=1
            nextmonth = 1
        else:
            nextmonth = current_date.month + 1
        context['nextmonth']= nextmonth
        context['monthly_payment_url'] = reverse('Monthly_Payment', kwargs={'year': context['year'], 'month': context['month']})
        payments = Payment.objects.filter(date__year=context['year'], date__month=context['month'])
        context['total_price'] = payments.aggregate(Sum('price'))['price__sum']
        payments_by_category = payments.values('category__name').annotate(category_total=Sum('price'))
        category_list = [{'category': payment['category__name'], 'total': payment['category_total']} for payment in payments_by_category]
        context['category_list'] = category_list
        return context

class transition(TemplateView):
    model = Payment
    template_name = "transition"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.now()
        context['current_year'] = current_date.year
        context['current_month'] = current_date.month
        return context