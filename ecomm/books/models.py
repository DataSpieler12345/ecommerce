from django.db import models

# Create your models here.
class Book(models.Model):
    # title
    title = models.CharField(max_length=255)
    # price
    price = models.FloatField()
    # cover
    cover = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title