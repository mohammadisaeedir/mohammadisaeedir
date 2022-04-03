from secrets import choice
from turtle import position, title
from django.db import models

# Create your models here.


class Options(models.Model):
    main_title = models.CharField(max_length=100)
    about_me = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Basic Options'


class ContactInfo(models.Model):
    choice_list = [('sn', 'Social Network'), ('glance', 'Glance'),
                   ('contact', 'Contact'), ('other', 'Others'), ]
    title = models.CharField(max_length=80)
    fontawesome = models.CharField(blank=True, max_length=100)
    value = models.CharField(max_length=200)
    contact_type = models.CharField(max_length=50, choices=choice_list)

    class Meta:
        verbose_name_plural = 'Contact Info'


class Skill(models.Model):
    category = models.CharField(max_length=60)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=80)
    start_date = models.DateField()
    current = models.BooleanField(default=False)
    finish_date = models.DateField(blank=True, null=True)
    body = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def duration(self):
        return self.finish_date - self.start_date


class Education(models.Model):
    university = models.CharField(max_length=100)
    level = models.CharField(max_length=40)
    major = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    logo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField()
    description = models.CharField(max_length=200)


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField()
    

class ContactForm(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=30, choices=[
                               ('public', 'Public'), ('cv', 'CV Request'), ('meeting', 'Meeting'), ('project', 'New Project')], default='public')
    body = models.TextField()
    review = models.TextField(blank=True)
    status = models.BooleanField(default=False)
