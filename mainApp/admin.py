from django.contrib import admin
from .models import User,Room,Topic,Message

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
