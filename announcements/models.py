from django.db import models

from common.models import BaseModel


class StatusChoices(models.TextChoices):
    IN_REVIEW = 'in_review'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    ARCHIVED = 'archived'


class Announcement(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.IN_REVIEW,
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title