from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.

class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        super().save()


class Page(Timestampable):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextField()

    def __str__(self):
        return self.title


def uploadEventPhoto(instance, filename):
    return "%s/%s/%s" % ('event', instance.title, filename)


class Event(Timestampable):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    photo = models.ImageField(upload_to=uploadEventPhoto,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.title


class Menu(Timestampable):
    title = models.CharField(max_length=255)
    url = models.URLField()
    priority = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['-priority']

    def __str__(self):
        return self.title


def uploadSliderPhoto(instance, filename):
    return "%s/%s/%s" % ('slider', str(instance.pk), filename)


class Slider(Timestampable):
    photo = models.ImageField(upload_to=uploadSliderPhoto,
                              null=True,
                              blank=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
