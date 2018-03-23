from django.contrib import admin

# Register your models here.
from .models import Question,Choice,Driver,Comment
from polls.models import Comment

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Driver)
admin.site.register(Comment) 


