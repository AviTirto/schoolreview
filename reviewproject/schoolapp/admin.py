from django.contrib import admin
from schoolapp import models
from .models import School, Comment

admin.site.register(models.School)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'school.name', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author.first_name', 'author.last_name' 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)