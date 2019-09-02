from django.contrib import admin
from mail.models import Inbox,Sentmail,Notification,Important
# Register your models here.
admin.site.register(Important)
admin.site.register(Inbox)
admin.site.register(Notification)
admin.site.register(Sentmail)