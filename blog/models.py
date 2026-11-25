from django.db import models

# Create your models here.

class articles(models.Model):

    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    content = models.TextField()

    def __str__(self):

        return self.title