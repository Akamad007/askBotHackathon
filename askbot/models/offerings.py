from django.db import models


class Offering(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    professor = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    term = models.CharField(max_length=200, blank=False, null=True)
    timings = models.CharField(max_length=200, blank=False, null=True)#Mon, Wed, Fri - 1.30
    updated = models.DateTimeField(auto_now_add=True)
