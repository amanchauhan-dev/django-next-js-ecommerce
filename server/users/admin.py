from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, BuyerProfile, SellerProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("role", "bio", "birth_date", "profile_picture")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(BuyerProfile)
admin.site.register(SellerProfile)
