from django.db import models
from django.forms import CharField
import string
import random

# Create your models here.


def generate_unique_code():
    length = 5
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if User.objects.filter(code=code).count() == 0:
            break
    return code


class User(models.Model):
    # id is already a part of the Model class!
    name = models.CharField(max_length=30, null=False)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    adminQ = models.BooleanField(null=False, default=False)
    code = models.CharField(max_length=50, default="", null=False)
