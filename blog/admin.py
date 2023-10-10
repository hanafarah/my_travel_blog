from django.contrib import admin
from . models import Topic, Post
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created','updated','status',)
    search_fields = ('title','author__username','author__first_name','author__last_name')
    list_filter = ('status', 'topics',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline,]

# @admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'created_on','updated_on','approved')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'text')

class CommentInline(admin.StackedInline):
    model = Comment
    readonly_fields = ('name', 'text', 'email', )
    can_delete = False
    extra = 0


admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Comment)