from django.contrib import admin
from .models import Articles


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author","moderation",)
    list_editable = ("moderation",)
    list_per_page = 5


admin.site.register(Articles, PostAdmin)


