from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER = [
        ("male","male"),
        ("female","female"),
        ("other","other"),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20,choices=GENDER)
    profile_picture = models.ImageField(upload_to="profiles/")
    address = models.TextField()
    city = models.CharField(max_length=20)
