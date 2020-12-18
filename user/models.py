from django.db import models
from django.contrib.auth.models import User

Gender_options = (
    ('M','Male'),
    ('F','Female'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True,max_length=50, null=True)
    age =   models.IntegerField(blank=True, null=True)
    gender = models.CharField(blank=True,max_length=1, choices=Gender_options, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)

    def __str__(self):
        return self.name