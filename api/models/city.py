from django.db import models
from django.contrib.auth import get_user_model

# Model for citys
class City(models.Model):
  name = models.CharField(max_length=100)
  favorite = models.BooleanField()
  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.name}"

  def as_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'favorite': self.favorite
    }
