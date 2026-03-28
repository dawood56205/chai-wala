from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CHAIVARIETY(models.Model):
  CHAI_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('EL', 'ELAICHI'),
    ('KI', 'KIWI'),
  ]
  
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default = timezone.now)
  type = models.CharField(max_length = 2, choices = CHAI_TYPE_CHOICE)
  descriptions = models.TextField(default = "empty")
  price = models.IntegerField(default = "10$")

  def __str__(self) :
    return self.name

# Create your models here.

# one to many
class chai_review(models.Model):
  rating_type = [
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
    (4, 'four'),
    (5, 'five')
  ]
  chai = models.ForeignKey(CHAIVARIETY, on_delete = models.CASCADE, related_name = 'reviews')
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  rating = models.CharField(max_length = 2, choices = rating_type)
  comment = models.TextField()
  date_added = models.DateTimeField(default = timezone.now)

  def __str__(self):
    return f'{self.user.username} review for{self.chai.name}'
  

# many to many
class stores(models.Model):
  name = models.CharField(max_length = 100)
  location = models.CharField(max_length = 100)
  chai_varieties = models.ManyToManyField(CHAIVARIETY, related_name = 'stores')

  def __str__(self):
    return self.name


# one to one
class chai_certificate(models.Model):
  chai = models.OneToOneField(CHAIVARIETY, on_delete = models.CASCADE, related_name = 'certificate')
  certificate_number = models.CharField(max_length = 100)
  issued_date = models.DateTimeField(default = timezone.now)
  valid_date = models.DateTimeField()

  def __str__(self):
    return f'certificate for {self.name.chai}'
