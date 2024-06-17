from django.contrib import admin
from .models import *
#admin.site.register(User)
#admin.site.register(MalleTag)
#admin.site.register(MalleTask)
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(MalleTag)
class MalleTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MalleTask)
class MalleTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'user')
    list_filter = ('completed', 'due_date', 'tags')
    search_fields = ('title', 'description')
    autocomplete_fields = ('user', 'tags')
