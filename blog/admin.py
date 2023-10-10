from django.contrib import admin
from . models import Topic, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created','updated','status',)
    search_fields = ('title','author__username','author__first_name','author__last_name')
    list_filter = ('status', 'topics',)
    prepopulated_fields = {'slug': ('title',)}

# @admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)