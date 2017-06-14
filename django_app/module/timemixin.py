from django.db import models

__all__ = [
    'TimeMixinStamp'
]


class TimeMixinStamp(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
