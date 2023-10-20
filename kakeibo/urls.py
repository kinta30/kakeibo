from django.urls import path
from . import views

urlpatterns = [
    path("",views.PaymentList.get_PaymentList(),name="Paymentlist"),
]