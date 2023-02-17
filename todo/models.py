from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=Falese, blank=False)
    done = models.BooleanField(null=Falese, blank=False, default=False)
