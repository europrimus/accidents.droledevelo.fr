from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.
class URL(models.Model):
    class CecksumTypes(models.TextChoices):
        SHA1 = 'sha1', gettext_lazy('sha1')

    class MimeTypes(models.TextChoices):
        CSV = 'text/csv', gettext_lazy('csv')
        PDF = 'application/pdf', gettext_lazy('pdf')
        JSON = 'application/json', gettext_lazy('json')

    uid = models.CharField(
        max_length=36, 
        unique=True
        )
    title = models.CharField(
        max_length=150
        )
    description = models.CharField(
        max_length=500,
        null=True
        )
    url = models.CharField(
        max_length=250
        )
    checksum_type = models.CharField(
        max_length=4,
        choices=CecksumTypes.choices,
        null=True
        )
    checksum_value = models.CharField(
        max_length=50,
        null=True
        )
    filesize = models.PositiveIntegerField(
        null=True
        )
    mime_type = models.CharField(
        max_length=16,
        choices=MimeTypes.choices,
        null=True
        )
    created_at = models.DateTimeField(
        null=True
        )
    published_at = models.DateTimeField(
        null=True
        )
    last_modified_at = models.DateTimeField(
        null=True
        )
    imported_at = models.DateTimeField(
        null=True
        )