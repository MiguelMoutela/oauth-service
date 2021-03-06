from django.db import models
from uuid import uuid4
import hashlib


def get_rand_hash():
    uid = uuid4()
    return hashlib.sha1(str(uid)).hexdigest()


class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=200, default=get_rand_hash)
    secret = models.CharField(max_length=200, default=get_rand_hash)

    def __unicode__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    favorite_color = models.CharField(max_length=20,
            help_text="English or hex")

    def __unicode__(self):
        return "User Profile for %s" % self.user.username
