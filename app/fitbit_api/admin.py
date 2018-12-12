from django.contrib import admin

from .models import Member, UserToken

admin.site.register(Member)
admin.site.register(UserToken)
