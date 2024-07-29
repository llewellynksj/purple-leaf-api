from django.db import models
from django.contrib.auth.models import User
from leaves.models import Leaf


class Remember(models.Model):
    """
    Remember model stores when a Leaf has been remembered (read and acknowledged) by another user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leaf = models.ForeignKey(
        Leaf, related_name='remembered', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} remembered {self.leaf.user}'s memory"
