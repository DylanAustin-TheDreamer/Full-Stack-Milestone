from django.shortcuts import render

def dashboard(request):
    """Dashboard view for applications"""
    return render(request, 'applications/dashboard.html')
