from django.urls import path, reverse
from . import views
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap

app_name = 'main'

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return [
            'main:home',
            'main:profile',
            'main:download',
            'main:rickroll',
        ]

    def location(self, item):
        return reverse(item)

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('profile/', views.profile, name='profile'),
    path('delete-account/confirm/', views.delete_account_confirm, name='delete_account_confirm'),
    path('delete-account/', views.delete_account, name='delete_account'),
    path('toggle-membership/', views.toggle_membership, name='toggle_membership'),
    path('download/', views.download, name='download'),
    path('download-app/', views.download_app, name='download_app'),
    path('add-review/', views.add_review, name='add_review'),
    path('edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('rickroll/', views.rickroll, name='rickroll'),
]