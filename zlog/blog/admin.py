from django.contrib import admin
from .models import BlogPost
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'overview',
        'created_at',
        'updated_at',
        'creator',
        'target_age'
    )
    search_fields = (
        'text',
        'title',
        'overview'
    )
    readonly_fields = (
        'created_at',
        'updated_at'
    )
    list_filter = (
        'target_age',
        'creator'
    )


admin.site.register(BlogPost, BlogPostAdmin)
