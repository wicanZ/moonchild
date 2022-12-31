from django.contrib import admin
#from base.forms import RegisterForm

# Register your models here.

from .models import (
    Note,
    Message,
    Blog ,
    User ,
    MindSet ,
    Ip ,
    Event,
    UserDetail
)
admin.site.register(User)
admin.site.register(Note)
#admin.site.register(ProfileUser)
admin.site.register(Message)

admin.site.register(Blog)

admin.site.register(MindSet)
admin.site.register(Ip)

admin.site.register(Event)
admin.site.register(UserDetail)