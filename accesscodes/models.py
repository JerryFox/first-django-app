from django.db import models

from django.contrib.auth.models import User

class Code(models.Model): 
    """codes for access system"""
    code_type = models.CharField(max_length=10, null=True, blank=True, default = None)
    keyb_number = models.CharField(max_length=15, null=True, blank=True, default=None)
    card_number = models.CharField(max_length=6, null=True, blank=True, default=None)
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_to = models.DateTimeField(null=True, blank=True, default = None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)


class Event(models.Model): 
    """events for access system"""
    event_type = models.CharField(max_length=10, null=True, blank=True, default = None) 
    short_description = models.CharField(max_length=10, unique=True) 
    long_description = models.CharField(max_length=200, null=True, blank=True, default = None) 
    event_begin = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)

    
