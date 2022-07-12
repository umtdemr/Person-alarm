from django.contrib import admin

from core.models import (
    SiteSettings,
    Image,
    ProcessedImage,
)


class SingletonAdmin(admin.ModelAdmin):
    actions = None

    def has_add_permission(self, request):
        permission = super().has_add_permission(request)
        if permission and not self.model.objects.count():
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SiteSettingsAdmin(admin.ModelAdmin):
    pass 


admin.site.register(SiteSettings, SiteSettingsAdmin)
admin.site.register(Image)
admin.site.register(ProcessedImage)
