from django.contrib import admin
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    
    fields = ('user'
              ,)

    

admin.site.register(Profile, ProfileAdmin)