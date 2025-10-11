from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    """Model to store user reviews"""

    user = models.CharField(max_length=200)
    main_content = models.TextField()
    rating = models.IntegerField()
    def __str__(self):
        return self.user


class UserProfile(models.Model):
    """Extended user profile to handle premium membership"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium_member = models.BooleanField(default=False)
    membership_start_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - {'Premium' if self.is_premium_member else 'Free'}"
    