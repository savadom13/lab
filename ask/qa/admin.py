from django.contrib import admin

from .models import Answer,Question,User,Session

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(User)
admin.site.register(Session)
