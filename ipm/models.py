from django.db import models


# Create your models here.
class UsersApi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name
