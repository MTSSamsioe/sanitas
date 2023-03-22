from django.contrib import admin
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    
    fields = (
              'preset_full_name',
              'preset_email',
              'preset_adress',
              'preset_post_code',
              'preset_city',
              )


    list_display = ('user', )

    

admin.site.register(Profile, ProfileAdmin)