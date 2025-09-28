from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
    context = {
        'user': request.user,
    }
    return render(request, 'main/profile.html', context)
