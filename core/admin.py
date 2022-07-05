from django.contrib import admin

from core.models import (
    SiteSettings,
    Image,
    ProcessedImage,
)


class SiteSettingsAdmin(admin.ModelAdmin):
    pass 


admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Image)
admin.site.register(ProcessedImage)
