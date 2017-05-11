from django.contrib import admin

from .models import MemoryMapKey, SignificantValue

@admin.register(MemoryMapKey)
class MemoryMapKeyAdmin(admin.ModelAdmin):
    fields = ('name', 'frequency')
    list_display = ('name', 'frequency')
    list_filter = ('name', 'frequency')


@admin.register(SignificantValue)
class SignificantValueAdmin(admin.ModelAdmin):
    fields = ('key', 'content', 'remark', 'related_type', 'images', 'supported')
    list_display = ('key', 'content', 'related_type', 'supported')
    list_filter = ('key', 'content', 'related_type', 'supported')
