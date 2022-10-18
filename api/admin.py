from django.contrib import admin
from .models import Task, Note


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_completed')
    list_editable = ('is_completed', )
    list_display_links = ('id', 'title', )


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'body')
    list_display_links = ('id', 'title', )


admin.site.register(Note, NoteAdmin)
admin.site.register(Task, TaskAdmin)
