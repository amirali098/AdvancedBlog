from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.



class CustomUserAdamin(UserAdmin):
    model=User
    list_display=('email','is_superuser','is_staff','is_active')
    list_filter=('email','is_superuser','is_staff','is_active')
    searching_filds= ('email',)
    ordering=('email',)
    fieldsets = (
       ("authentication",{"fields":("email", "password")}),
       ("permissions",{"fields":("is_staff","is_active","is_superuser","is_verified")}),
       ("Group Permissions",{"fields":("groups", "user_permissions")}),
       ("Important Dates",{"fields":("last_login",)})
    )
    
    add_fieldsets=(
        ("None",{"classes":("wide",),
                 "fields":("password","password2","email","is_staff","is_superuser","is_active")}),
    )

admin.site.register(User,CustomUserAdamin)