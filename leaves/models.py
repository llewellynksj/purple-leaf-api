from django.db import models
from django.contrib.auth.models import User

class Leaf(models.Model):
  LOSS_TYPE = [
    ('during', 'Loss during pregnancy'),
    ('at or after', 'Loss at birth or shortly after' ),
  ]
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  loss_type = models.CharField(max_length=100, choices=LOSS_TYPE, blank=True)
  name = models.CharField(max_length=100, blank=True, null=True, help_text='Had you picked out a name or nickname?')
  parent_name1 = models.CharField(max_length=100, blank=True, null=True)
  parent_name2 = models.CharField(max_length=100, blank=True, null=True)
  dob_due_date = models.DateField()
  weight = models.IntegerField(help_text='kilograms')
  image = models.ImageField(
      upload_to='images/',
      default='../default_post_rgq6aq'
  )
  memory = models.TextField(blank=True, null=True, help_text='Some families find it helpful to write a message directly to their lost loved one, or to share a memory. This should be whatever you will find helpful to your healing journey.')

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return f"{self.owner}'s leaf, added on {self.created_at}"
