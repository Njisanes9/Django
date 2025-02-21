from django.db import models

# Create your models here.

class MyModel(models.Model):
    name = models.TextField(max_length=100)
    surname = models.TextField()
    dob = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name