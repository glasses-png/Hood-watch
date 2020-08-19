from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.
# 
class NeighbourHood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=60)
  admin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hood')
  hood_logo = models.ImageField(upload_to='images/')
  description = models.TextField()
  health_tell = models.IntegerField(null=True, blank=True)
  police_number = models.IntegerField(null=True,blank=True)

  def __str__(self):
    return f'{self.name} hood'

  def create_neighbourhood(self):
    self.save()

  def delete_neighbourhood(self):
    self.delete()

  @classmethod
  def find_neighborhood(cls, neighborhood_id):
    return cls.objects.filter(id=neighborhood_id)

class Users(models.Model):
    user_id = models.PositiveIntegerField(null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=100)
    status = models.TextField(max_length=100)
    neighborhood_id = models.ForeignKey(NeighbourHood,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name.username) 

class Business(models.Model):
    name = models.TextField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood_id = models.ForeignKey(NeighbourHood,default=None, on_delete=models.CASCADE)
    email = models.TextField(max_length = 100)

    def __str__(self):
        return self.name



class Post(models.Model):
  title = models.CharField(max_length=120, null=True)
  post = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
  hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood_post')
