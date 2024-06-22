from django.db import models


class News(models.Model):
  head = models.CharField(max_length=50)
  body = models.TextField()


  def __str__(self):
    return self.head
  
