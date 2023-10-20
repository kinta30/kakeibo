from django.urls import path
from .views import PaymentList,IncomeList

urlpatterns = [
    path("",views.index,name="Paymentlist"),
    path("",views.index,name="IncomeList"),
]