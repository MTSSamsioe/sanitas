from django.contrib import admin
from .models import Pt_sessions, Subscriptions


# Register your models here.
class Pt_sessionsAdmin(admin.ModelAdmin):
    list_display =(
        
        'name',
    )
ordering = ('user,')

class SubscriptionsAdmin(admin.ModelAdmin):
    list_display =(
        
        'name',
    )
ordering = ('user,')

admin.site.register(Pt_sessions, Pt_sessionsAdmin)
admin.site.register(Subscriptions, SubscriptionsAdmin)