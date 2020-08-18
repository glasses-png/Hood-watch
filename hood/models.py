from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user_id = models.PositiveIntegerField(null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.TextField(max_length=100)
    status = models.TextField(max_length=100)
    neighborhood_id = models.ForeignKey(Neighborhood,default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name.username) 

class Business(models.Model):
    name = models.TextField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood_id = models.ForeignKey(Neighborhood,default=None, on_delete=models.CASCADE)
    email = models.TextField(max_length = 100)

    def __str__(self):
        return self.name