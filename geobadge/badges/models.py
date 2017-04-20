from django.db import models
from django.utils import timezone


class Badge(models.Model):

    created = models.DateTimeField(
        default=timezone.now,
        help_text='The date on which the badge was created.'
    )
