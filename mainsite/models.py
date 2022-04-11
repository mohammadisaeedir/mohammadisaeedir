import json
from django.db import models
from datetime import date
from ckeditor_uploader.fields import RichTextUploadingField


class Options(models.Model):
    main_title = models.CharField(max_length=100)
    about_me = models.TextField()
    image = models.ImageField(upload_to='images')
    color = models.CharField(max_length=8, default=None, blank=True)

    def __str__(self):
        return 'Basic Options'

    class Meta:
        verbose_name_plural = 'Basic Options'


class ContactInfo(models.Model):
    choice_list = [('sn', 'Social Network'), ('glance', 'Glance'),
                   ('mail', 'Email'), ('phone', 'Phone'), ('others', 'Others'), ]
    title = models.CharField(max_length=80)
    fontawesome = models.CharField(blank=True, max_length=100)
    value = models.CharField(max_length=200)
    contact_type = models.CharField(max_length=50, choices=choice_list)

    def __str__(self):
        return f'{self.title} | {self.value}'

    class Meta:
        verbose_name_plural = 'Contact Info'


class SkillCategory(models.Model):
    title = models.CharField(unique=True, max_length=60)

    def __str__(self):
        return self.title


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory, on_delete=models.SET_NULL, null=True, related_name='skills')
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category} | {self.title}'


class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=80)
    start_date = models.DateField()
    finish_date = models.DateField(blank=True, null=True)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.company} | {self.position}'

    def positions():
        ls = []
        positions = Experience.objects.all()
        for item in positions:
            ls.append(item.position)
        return json.dumps(ls)

    def duration(self):
        if self.finish_date:
            result = self.finish_date - self.start_date
        else:
            result = date.today() - self.start_date
        years, remain = divmod(result.days, 365)
        month, days = divmod(remain, 30)

        return f'{years} years, {month} months'


class Education(models.Model):
    university = models.CharField(max_length=100)
    level = models.CharField(max_length=40)
    major = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    logo = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.major} | {self.university}'


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.title}'


class ContactForm(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=30, choices=[
                               ('public', 'Public'), ('cv', 'CV Request'), ('meeting', 'Meeting'), ('project', 'New Project')], default='public')
    body = models.TextField()
    review = models.TextField(blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.subject} | {self.user_name}'
