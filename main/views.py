from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import UserProfile

def home(request):
    """Homepage view"""
    context = {
        'page_title': 'Welcome to Python App Downloads',
        'featured_apps': [],  # Will be populated later with actual data
        'recent_reviews': [],  # Will be populated later with actual data
    }
    return render(request, 'main/home.html', context)

@login_required
def profile(request):
    """User profile view"""
    # Get or create the profile if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    context = {
        'user': request.user,
    }
    return render(request, 'main/profile.html', context)

@login_required
def delete_account_confirm(request):
    """Show account deletion confirmation page"""
    return render(request, 'main/delete_account_confirm.html')

@login_required
@require_POST
def delete_account(request):
    """Handle account deletion"""
    user = request.user
    username = user.username
    
    # Log the user out first
    logout(request)
    
    # Delete the user account
    user.delete()
    
    # Add a success message
    messages.success(request, f'Account "{username}" has been successfully deleted.')
    
    # Redirect to home page
    return redirect('main:home')

# In your views.py
@login_required
def toggle_membership(request):
    if request.method == 'POST':
        # Get or create the profile if it doesn't exist
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.is_premium_member = not profile.is_premium_member  # Toggle it
        profile.save()
    return redirect('main:profile')