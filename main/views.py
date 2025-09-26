from django.shortcuts import render

def home(request):
    """Homepage view"""
    context = {
        'page_title': 'Welcome to Python App Downloads',
        'featured_apps': [],  # Will be populated later with actual data
        'recent_reviews': [],  # Will be populated later with actual data
    }
    return render(request, 'main/home.html', context)
