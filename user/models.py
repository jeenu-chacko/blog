from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

Gender_options = (
    ('M','Male'),
    ('F','Female'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(blank=True,max_length=50, null=True)
    age =   models.IntegerField(blank=True, null=True)
    gender = models.CharField(blank=True,max_length=1, choices=Gender_options, null=True)
    linkedin_Url= models.CharField(blank=True,max_length=100, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title