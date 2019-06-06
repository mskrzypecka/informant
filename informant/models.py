from django.db import models
from django.utils import timezone
from .helpers import TransportChoice

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    transport = models.CharField(
      max_length=25,
      choices=[(tag.name, tag.value) for tag in TransportChoice],
      default=TransportChoice.BOTH
      )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('informant.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text