from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'contact'


# class Hero(models.Model):
#     name = models.CharField(max_length=200)
#     heros_image = models.ImageField(upload_to='hero')

#     def __str__(self):
#         return self.name
