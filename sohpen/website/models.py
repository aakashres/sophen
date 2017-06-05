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
    url = models.CharField(max_length=50, help_text='/pages/1/')
    priority = models.IntegerField(
        help_text='Lower number comes first in menu', null=False, blank=False)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey(
        'self', related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ['priority', ]

    @staticmethod
    def get_root():
        return Menu.objects.filter(title="root").get()

    def not_deleted_children(self):
        return self.children.filter(deleted_at=None)

    def __str__(self):
        if self.parent:
            if self.parent.title != "root":
                return self.parent.title + ' : ' + self.title
        return self.title


def uploadSliderPhoto(instance, filename):
    date_time = str(timezone.now())
    return "%s/%s/%s" % ('slider', str(date_time), filename)


class Slider(Timestampable):
    photo = models.ImageField(upload_to=uploadSliderPhoto,
                              null=True,
                              blank=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


def uploadGalleryPhoto(instance, filename):
    date_time = str(timezone.now())
    return "%s/%s/%s" % ('gallery', str(date_time), filename)


class Gallery(Timestampable):
    photo = models.ImageField(upload_to=uploadGalleryPhoto,
                              null=True,
                              blank=True)
    caption = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return str(self.pk)


def uploadFile(instance, filename):
    date_time = str(timezone.now())
    return "%s/%s/%s" % ('file', str(date_time), filename)


class File(Timestampable):
    file = models.FileField(upload_to=uploadFile,
                            null=True,
                            blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Member(Timestampable):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=100)
    dob = models.DateField()
    photo = models.ImageField()
    permanent_address = models.CharField(max_length=255)
    mailing_address = models.CharField(max_length=255)
    degree_1 = models.CharField(max_length=100)
    major_1 = models.CharField(max_length=100)
    institution_1 = models.CharField(max_length=100)
    year_1 = models.CharField(max_length=4)
    degree_2 = models.CharField(max_length=100, null=True, blank=True)
    major_2 = models.CharField(max_length=100, null=True, blank=True)
    institution_2 = models.CharField(max_length=100, null=True, blank=True)
    year_2 = models.CharField(max_length=4, null=True, blank=True)
    degree_3 = models.CharField(max_length=100, null=True, blank=True)
    major_3 = models.CharField(max_length=100, null=True, blank=True)
    institution_3 = models.CharField(max_length=100, null=True, blank=True)
    year_3 = models.CharField(max_length=4, null=True, blank=True)
    degree_4 = models.CharField(max_length=100, null=True, blank=True)
    major_4 = models.CharField(max_length=100, null=True, blank=True)
    institution_4 = models.CharField(max_length=100, null=True, blank=True)
    year_4 = models.CharField(max_length=4, null=True, blank=True)
    from_1 = models.DateField()
    to_1 = models.DateField()
    organization_1 = models.CharField(max_length=255)
    description_of_work_1 = models.CharField(max_length=255)
    from_2 = models.DateField(null=True, blank=True)
    to_2 = models.DateField(null=True, blank=True)
    organization_2 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_2 = models.CharField(
        max_length=255, null=True, blank=True)
    from_3 = models.DateField(null=True, blank=True)
    to_3 = models.DateField(null=True, blank=True)
    organization_3 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_3 = models.CharField(
        max_length=255, null=True, blank=True)
    from_4 = models.DateField(null=True, blank=True)
    to_4 = models.DateField(null=True, blank=True)
    organization_4 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_4 = models.CharField(
        max_length=255, null=True, blank=True)
    from_5 = models.DateField(null=True, blank=True)
    to_5 = models.DateField(null=True, blank=True)
    organization_5 = models.CharField(max_length=255, null=True, blank=True)
    description_of_work_5 = models.CharField(
        max_length=255, null=True, blank=True)
    membership_of_any_other = models.CharField(
        max_length=255, null=True, blank=True)
    present_position = models.CharField(max_length=255, null=True, blank=True)
    employeer = models.CharField(max_length=255, null=True, blank=True)
    office_address = models.CharField(max_length=255, blank=True, null=True)
    recommenders_name = models.CharField(max_length=255, null=True, blank=True)
    membership_no = models.IntegerField(null=True, blank=True)
    membership_status = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.first_name + ' ' + self.last_name)
