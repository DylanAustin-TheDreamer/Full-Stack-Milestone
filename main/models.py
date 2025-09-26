from django.db import models

# Create your models here.
class Review(models.Model):
    user = models.CharField(max_length=200)
    main_content = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.user