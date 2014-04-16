

from django.db import models


class SortableModel(models.Model):

    sort_order = models.PositiveIntegerField('Order', default=0)

    class Meta:
        abstract = True
        ordering = ('sort_order',)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-modified', '-created',)
