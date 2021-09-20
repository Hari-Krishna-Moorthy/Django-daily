from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
