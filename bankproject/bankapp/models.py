from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)



class register(models.Model):
        username = models.CharField(max_length=250)
        password = models.CharField(max_length=250)

class Branches(models.Model):
            name = models.CharField(max_length=250, unique=True)
            slug = models.SlugField(max_length=250, unique=True)



class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Branches, on_delete=models.CASCADE)

