from django.db import models

# Create your models here.
class NeighbourHood(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=60)
  admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
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