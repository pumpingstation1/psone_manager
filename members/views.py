from django.db.models import Q
from django.views.generic import ListView
from .models import UserProfile

class MemberSearch(ListView):
    context_object_name = 'user_profile'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            users = UserProfile.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(nickname__icontains=query) |
                Q(paypal_email__icontains=query) |
                Q(contact_email__icontains=query)
            )
        else:
            users = UserProfile.objects.filter(pk=0)
        return users

        
