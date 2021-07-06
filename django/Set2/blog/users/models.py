from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=255
    )
    featured_image = models.ImageField(
        null = True,
        blank=True,
        upload_to='featured_images'
    )
    content = models.TextField()
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
        )
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(
        to=User,
        blank=True,
        related_name = 'likes'
    )

    def __str__(self):
        return f'Post {self.id}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
