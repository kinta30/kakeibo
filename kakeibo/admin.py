from django.contrib import admin
from .models import PaymentCategory, IncomeCategory, Payment, Income

# Register your models here.
admin.site.register(PaymentCategory)
admin.site.register(IncomeCategory)
admin.site.register(Payment)
admin.site.register(Income)