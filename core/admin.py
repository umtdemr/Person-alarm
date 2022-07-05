from django.contrib import admin

from core.models import SiteSettings


class SiteSettingsAdmin(admin.ModelAdmin):
    pass 


admin.site.register(SiteSettings, SiteSettingsAdmin)
