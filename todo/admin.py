from django.contrib import admin
from .models import Tag, Task


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'deadline', 'is_done')
    list_filter = ('is_done', 'created_at', 'deadline')
    search_fields = ('content',)
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)


admin.site.register(Tag, TagAdmin)
admin.site.register(Task, TaskAdmin)
