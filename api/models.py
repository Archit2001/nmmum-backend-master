from django.core.checks.messages import CRITICAL
from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.files import File
from django.utils.safestring import mark_safe
import uuid
from PIL import Image
from .utils import resize_image

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(upload_to ='images/')
    url = models.ImageField(upload_to='images/', null=True, blank=True)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    at_home = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return str(f"{self.year}-{uuid.uuid4()}")

    def save(self, *args, **kwargs):
        self.url = resize_image(self.image)
        super().save(*args, **kwargs)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))
        

class Resource(models.Model):

    class ResourceTypes(models.TextChoices):
        PDF = 'PDF', _('PDF')

    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    type = models.CharField(max_length=3, choices=ResourceTypes.choices, default=ResourceTypes.PDF)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Team(models.Model):

    class TeamTypes(models.TextChoices):
        SECRETARIAT = 'SECRETARIAT', _('Secretariat')
        DIRECTORATE = 'DIRECTORATE', _('Directorate')

    image = models.ImageField(upload_to ='images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(  max_length=11,choices=TeamTypes.choices, default=TeamTypes.SECRETARIAT)
    position = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url = resize_image(self.image, q=60)
        super().save(*args, **kwargs)
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="150"/>'.format(self.image.url))

    def __str__(self):
        return str(f"{self.name}-{uuid.uuid4()}")


class Event(models.Model):
    description = models.TextField(max_length=300)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f'{self.description[:100]} - {self.created_at}')


class Committee(models.Model):
    image = models.ImageField(upload_to ='images/')
    info = models.TextField()
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name= models.CharField(max_length=100)
    image_cover = models.ImageField(upload_to ='images/')
    content = models.TextField()
    published_at = models.DateTimeField(null=True , blank=True)
    published = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url = resize_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class About(models.Model):
    name= models.CharField(max_length=50)
    image = models.ImageField(upload_to ='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.name


class Recent(models.Model):
    alternate_text = models.CharField(max_length=50, null=True, blank=True, default=uuid.uuid4())
    image = models.ImageField(upload_to ='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url = resize_image(self.image)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.alternate_text


class Notifications (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    trigger_at = models.DateTimeField()
    triggered= models.BooleanField(default=False)
    
    class NotificationType(models.TextChoices):
        NORMAL = 'NORMAL', _('Normal')
        CRITICAL = 'CRITICAL', _('Critical')

    priority = models.CharField( max_length=8, choices=NotificationType.choices, default=NotificationType.NORMAL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f'{self.title} - {self.description[:100]}'

class FirebaseToken(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token=models.CharField(max_length=256)

    def __str__(self):
        return self.token[:80]



