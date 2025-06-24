from django.contrib import admin
from .models import LocalNews, Device
from .utils import send_fcm_v1_notification

class LocalNewsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Only send notification when creating (not updating)
        if not change:
            device_tokens = [d.token for d in Device.objects.all()]
            send_fcm_v1_notification(
                tokens=device_tokens,
                title=obj.title,
                body=obj.short_description
            )

admin.site.register(LocalNews, LocalNewsAdmin)
admin.site.register(Device)
