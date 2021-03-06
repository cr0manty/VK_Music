from django.contrib import admin

from .models import Log, RQLog, TelegramBotLogs, TelegramLogs


class ReadOnlyAdminMixin(object):
    list_display = ('from_user', 'created_at')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Log)
class LogAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    pass


@admin.register(RQLog)
class RQLogAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_filter = ('is_exception',)


@admin.register(TelegramBotLogs)
class TelegramBotLogsAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('username', 'created_at')
    list_filter = ('log_type', 'language')


@admin.register(TelegramLogs)
class TelegramLogsAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ('username', 'created_at')
    list_filter = ('created_at', 'language', 'is_group')