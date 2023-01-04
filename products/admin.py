from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ["author", "text", "stars", "active"]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["title", "price", "active", ]

    inlines = [
        CommentInline,
    ]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ["author", "product", "active", "text", ]
