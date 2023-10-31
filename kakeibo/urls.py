from django.urls import path
from . import views

urlpatterns = [
    path("",views.PaymentList.as_view(),name="Paymentlist"),
]