from django.contrib import admin

# Register your models here.

from Comments.Model.comments_model import CommentModel 

admin.site.register(CommentModel)