from django.contrib import admin
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.ipn.admin import PayPalIPNAdmin
from .models import UserProfile

def save_payment_to_profile(modeladmin, request, queryset):
    for obj in queryset.order_by('payment_date'):
        paypal_to_profile(sender)

class MyPayPalIPNAdmin(PayPalIPNAdmin):
    action = [save_payment_to_profile]

admin.site.register(UserProfile)
admin.site.unregister(PayPalIPN)
admin.site.register(PayPalIPN, MyPayPalIPNAdmin)
