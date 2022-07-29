from django.contrib import admin
from .models import *
# Register your models here.


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'completed', 'cancelled')


admin.site.register(TodoItem, TodoItemAdmin)
