from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
