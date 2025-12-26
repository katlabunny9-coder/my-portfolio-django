from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    

    def __str__(self):
        return self.title
