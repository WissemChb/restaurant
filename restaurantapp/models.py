# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Restaurant(models.Model):
    name        = models.CharField(max_length = 50)
    location    = models.CharField(max_length = 50 , null= True, blank = True)

