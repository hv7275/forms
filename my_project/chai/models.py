from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
  
# OneToMany
class ChaiReciews(models.Model):
  
  chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField(
    validators=[
      MinValueValidator(1),
      MaxValueValidator(5),
    ],
    help_text='Rating must be bteween 1 to 5'
  )
  comment = models.TextField()
  craeted_at = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return f'{self.user.username} review for {self.chai.name}'
  

# many to many
class Store(models.Model):
  name = models.CharField(max_length=100)
  locations = models.CharField(max_length=100)
  
  chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores') # related_name is used to use this model in different model
  
  def __str__(self):
    return self.name
  
# one to one filed
# Let suppose we are giving a certificate for chai.
# there is one ceritificate is associated with only one chai type.

class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
  cerficate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_until = models.DateTimeField()
  
  def __str__(self):
    return f'Certificate for {self.chai.name}'