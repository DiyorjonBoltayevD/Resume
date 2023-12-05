from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     name = models.CharField(max_length=221)
#
#     def __str__(self):
#         return self.name


class AboutModel(models.Model):
    objects = None
    name = models.CharField(max_length=221)
    country = models.CharField(max_length=221)
    image = models.ImageField(upload_to='home/')
    code = models.IntegerField()
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField()
    data_of_birth = models.DateField()
    phone = models.CharField(max_length=221)
    project = models.IntegerField()

    def __str__(self):
        return self.name


class ResumeModel(models.Model):
    objects = None
    year = models.CharField(max_length=221)
    title = models.CharField(max_length=221)
    place = models.CharField(max_length=221)
    content = models.CharField(max_length=221)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


ICON_CHOICES = (
    ('analysis', "analysis"),
    ('flasks', 'flasks'),
    ('ideas', 'ideas')
)


class ServisModel(models.Model):
    objects = None
    icon = models.CharField(max_length=221, choices=ICON_CHOICES)
    profession = models.CharField(max_length=221)

    def __str__(self):
        return self.profession


class Myskills(models.Model):
    objects = None
    skil_name = models.CharField(max_length=221)
    percent = models.IntegerField()

    def __str__(self):
        return self.skil_name


class OurProjects(models.Model):
    objects = None
    picture = models.ImageField(upload_to='projects/')
    title = models.CharField(max_length=221)
    direction = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Ourblog(models.Model):
    objects = None
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='ourblog/')
    title = models.CharField(max_length=221)
    content = models.CharField(max_length=221)
    chat = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    awards = models.IntegerField()
    complateprojects = models.IntegerField()
    happy_customers = models.IntegerField()
    cups_of_coffe = models.IntegerField()

    def __str__(self):
        return self.title


class ContactModel(models.Model):
    objects = None
    name = models.CharField(max_length=221)
    telegram = models.CharField(max_length=221)
    address = models.CharField(max_length=221)
    phone = models.CharField(max_length=221)
    website = models.CharField(max_length=221)
    subject = models.CharField(max_length=221)
    message = models.CharField(max_length=221)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactModelMessage(models.Model):
    name = models.CharField(max_length=221)
    subject = models.CharField(max_length=221)
    message = models.CharField(max_length=221)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
