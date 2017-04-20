from django.contrib import admin
from geobadge.badges.models import Badge


class BadgeAdmin(admin.ModelAdmin):
    list_display = (
        'created',
    )


admin.site.register(Badge, BadgeAdmin)