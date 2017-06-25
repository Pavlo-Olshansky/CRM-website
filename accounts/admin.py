from django.contrib import admin
from .models import Account, Comment

admin.site.register(Account)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)
