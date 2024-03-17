from django.contrib import admin
from django.contrib import admin
from .models import *

# Register your models here.
# AUTH USER
class AuthUserAdmin(admin.ModelAdmin) :
    list_display = ('id','username','email','date_joined','is_active')
admin.site.register(AuthUser,AuthUserAdmin)