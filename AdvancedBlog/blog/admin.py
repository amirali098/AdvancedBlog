from django.contrib import admin
from .models import Post,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
        list_display=["title","author"]
        exclude = ["published_date"]





admin.site.register(Post,PostAdmin)
admin.site.register(Category)