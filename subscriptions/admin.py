from django.contrib import admin
from .models import Membership



class MembershipAdmin(admin.ModelAdmin):
    
    fields = (
        'user',
        'customer',
        'subscription',
        
        )
    
    
    list_display = ('user',
    'customer', 'subscription')

    

admin.site.register(Membership, MembershipAdmin)