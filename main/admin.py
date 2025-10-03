from django.contrib import admin
from .models import UserProfile, Review

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_premium_member', 'membership_start_date')
    list_filter = ('is_premium_member',)
    search_fields = ('user__username', 'user__email')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'main_content')
    list_filter = ('rating',)
    search_fields = ('user', 'main_content')

