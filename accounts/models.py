from django.db import models

# Create your models here.
class AccessCode(models.Model):
  Code = models.CharField(max_length=15)
  
  def __unicode__(self):
    return self.code