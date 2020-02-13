from django.db import models

# Create your models here.
class Product(models.Model):

    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, default="")
    price = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name




