from django.db import models
from django.utils import timezone

class ChaiVarity(models.Model):
  
  CHAI_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('EL', 'ELAICHI'),
    ('PL', 'PALNE'),
    ('KL', 'KIWI'),
  ]
  
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chai/varity/')
  created_at = models.DateTimeField(default=timezone.now)
  chai_type = models.CharField(max_length=2, choices=CHAI_CHOICE)
  description = models.TextField(blank=True, null=True)
  price = models.IntegerField(default=10)
  
  def __str__(self):
    return self.name