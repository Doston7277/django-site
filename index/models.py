from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.TextField()
    image = models.ImageField()
    project_type = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.TextField()
    body = models.TextField()
    url = models.TextField()
    background = models.ImageField()

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.TextField()
    job = models.TextField()
    image = models.ImageField()
    instagram = models.TextField()
    telegram = models.TextField()
    facebook = models.TextField()
    
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.TextField()
    icon = models.ImageField()

    def __str__(self):
        return self.name

class Feature(models.Model):
    title = models.TextField()
    body = models.TextField()
    icon = models.ImageField()
    url = models.TextField()

    def __str__(self):
        return self.title

class Setting(models.Model):
    logo = models.ImageField()
    about_title = models.TextField()
    about_body = models.TextField()
    about_text = models.TextField()
    subscribe_title = models.TextField()
    subscribe_body = models.TextField()
    subscribe_text = models.TextField()
    project_title = models.TextField()
    project_body = models.TextField()
    team_title = models.TextField()
    team_body = models.TextField()
    contact_title = models.TextField()
    contact_body = models.TextField()
    contact_phone = models.TextField()
    contact_phone_icon = models.ImageField()
    contact_email = models.TextField()
    contact_email_icon = models.ImageField()
    contact_site = models.TextField()
    contact_site_icon = models.ImageField()
    footer_text = models.TextField()
    footer_instagram_url = models.TextField()
    footer_telegram_url = models.TextField()
    footer_facebook_url = models.TextField()