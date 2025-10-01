from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import UserProfile, Review
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):
    """Homepage view"""
    context = {
        'page_title': 'Welcome to Python App Downloads',
        'featured_apps': [],  # Will be populated later with actual data
        'recent_reviews': get_recent_reviews(),  # Get real reviews from database
    }
    return render(request, 'main/home.html', context)

def download(request):
    """Download page view"""
    return render(request, 'main/download.html')

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

def get_recent_reviews():
    # Get the 3 most recent reviews from the database
    recent_reviews = Review.objects.all().order_by('-id')[:3]
    return [
        {
            'author': review.user, 
            'text': review.main_content, 
            'rating': review.rating
        } 
        for review in recent_reviews
    ]

def add_review(request):
    if request.method == 'POST':
        # Use logged-in username if available, otherwise use form input
        if request.user.is_authenticated:
            author = request.user.username
        else:
            author = request.POST.get('author')
            
        text = request.POST.get('text')
        rating = int(request.POST.get('rating', 0))
        
        # Save the review to the database
        review = Review.objects.create(
            user=author,  # Using the author name as user field
            main_content=text,
            rating=rating
        )
        
        messages.success(request, 'Thank you for your review!')
        return redirect('main:home')
    else:
        return redirect('main:home')
    

@login_required
def download_app(request):
    # Check if user has premium membership
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if profile.is_premium_member:
        # Redirect to Google Drive DIRECT download link
        download_url = "https://drive.google.com/uc?export=download&id=1sDfG8Q2y221eArnszSyW02-xq_VY_HG1"
        return HttpResponseRedirect(download_url)
    else:
        messages.error(request, "Premium membership required for downloads.")
        return redirect('main:profile')