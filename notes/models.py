# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=140, blank=True, default='')
