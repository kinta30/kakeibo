from django.urls import path
from .import view

urlpatterns = [
    path("",paymentlist.as_view(),name="paymentlist"),
]