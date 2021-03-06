from django.contrib import admin
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.ipn.admin import PayPalIPNAdmin
from .models import UserProfile, paypal_to_profile

def save_payment_to_profile(modeladmin, request, queryset):
    for obj in queryset.order_by('payment_date'):
        paypal_to_profile(obj)

class MyPayPalIPNAdmin(PayPalIPNAdmin):
    actions = [save_payment_to_profile]
    search_fields = ["txn_id", "recurring_payment_id", 'payer_email']

admin.site.register(UserProfile)
admin.site.unregister(PayPalIPN)
admin.site.register(PayPalIPN, MyPayPalIPNAdmin)
