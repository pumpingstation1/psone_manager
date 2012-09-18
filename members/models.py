import datetime
from django.db import models
from django.contrib.auth.models import User
from paypal.standard.ipn.signals import recurring_payment

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=50, blank=True)
    contact_email = models.EmailField(blank=True)
    paypal_email = models.EmailField(blank=True)
    paypal_id = models.CharField(max_length=13, blank=True)
    member_since = models.DateField(blank=True)
    member_until = models.DateField(blank=True)

def paypal_to_profile(sender, **kwargs):
    ipn_obj = sender
    # XXX assumption - paypal's payer id is constant for any paypal account [needs verification]
    (profile, created) = UserProfile.objects.get_or_create(paypal_id=ipn_obj.payer_id)
    profile.first_name = ipn_obj.first_name
    profile.last_name = ipn_obj.last_name
    profile.paypal_email = ipn_obj.payer_email
    payment_date = ipn_obj.payment_date
    if created:
        start_date = datetime.date(payment_date.year, payment_date.month, payment_date.day)
        profile.member_since = start_date
    end_date = datetime.date(payment_date.year, (payment_date.month+1)%12, payment_date.day)
    profile.member_until = end_date
    profile.save()

recurring_payment.connect(paypal_to_profile)
