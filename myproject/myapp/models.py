from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Work(models.Model):
    LINK_TYPE_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    ]
    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=LINK_TYPE_CHOICES)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)
    
@receiver(post_save, sender=User)
def create_artist_for_new_user(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(user=instance, name=instance.username)
