from django.contrib import admin
from . models import Topic, Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created','updated','status',)
    search_fields = ('title','author__username','author__first_name','author__last_name')
    list_filter = ('status', 'topics',)
    prepopulated_fields = {'slug': ('title',)}

# @admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'created','updated','approved')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)