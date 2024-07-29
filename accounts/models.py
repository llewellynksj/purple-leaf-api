from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Account(models.Model):
  """
  Account model stores user information
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=100)
  image = models.ImageField(
      upload_to='images/',
      default='../default_profile'
  )

  class Meta:
      ordering = ['-created_at']

  def __str__(self):
      return self.user.username

# Automatically create account when a new user is registered
def create_account(sender, instance, created, **kwargs):
  if created:
      Account.objects.create(user=instance)


post_save.connect(create_account, sender=User)
