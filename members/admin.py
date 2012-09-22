from django.contrib import admin
from .models import UserProfile

def save_payment_to_profile(modeladmin, request, queryset):
    for obj in queryset.order_by('payment_date'):
        paypal_to_profile(sender)

class UserProfileAdmin(admin.ModelAdmin):
    action = [save_payment_to_profile]

admin.site.register(UserProfile)
