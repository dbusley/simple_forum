# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Forum(models.Model):
    topic = models.CharField(max_length=255)


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Post(models.Model):
    message = models.TextField()
    forum = models.ForeignKey(Forum)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
