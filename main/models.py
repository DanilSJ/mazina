from django.db import models

class Shirt(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    company = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    top = models.BooleanField(default=False, null=True)
    img = models.ImageField(upload_to="img")
    
    def __str__(self):
        return self.name

class Shorts(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    company = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    top = models.BooleanField(default=False, null=True)
    img = models.ImageField(upload_to="img")
    
    def __str__(self):
        return self.name

class Sneakers(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    company = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    top = models.BooleanField(default=False, null=True)
    img = models.ImageField(upload_to="img")
    
    def __str__(self):
        return self.name
