from django.db import models
from django.template.context_processors import request

from common.models import BaseModel


def default_user(request):
    return request.user


class StatusChoices(models.TextChoices):
    IN_REVIEW = 'in_review'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    ARCHIVED = 'archived'


class Announcement(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.IN_REVIEW,
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
