from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AppUser(User):
    profile_pic = models.ImageField(null=True)
    bio = models.TextField(null=True, max_length=150)
    

    def __str__(self):
        return f'{self.username}'


class TaskToDo(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=250, null=True)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
    