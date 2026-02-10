from django.db import models
from django_resized import ResizedImageField
from django.core import signing

# Create your models here.
class Information(models.Model):
    info_id = models.AutoField(primary_key=True)
    intro = models.TextField()
    address = models.TextField()
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    email_add = models.CharField(max_length=30, blank=True, null=True)
    # resume = models.FileField(upload_to='resume/')
    # image = ResizedImageField(force_format="WEBP", quality=100, upload_to='me/')

    class Meta:
        db_table = "personal_information"


class Project(models.Model):
    proj_id = models.AutoField(primary_key=True)
    proj_name = models.CharField(max_length=100, verbose_name="Name")
    proj_desc = models.TextField(verbose_name="Description")
    proj_url = models.URLField(max_length=255, blank=True, null=True)
    proj_languages = models.JSONField(blank=True, null=True)
    proj_image = ResizedImageField(force_format="WEBP", quality=100, upload_to='projects-img/')
    proj_pdf = models.FileField(upload_to='projects-pdfs/') 
    year = models.CharField(max_length=4, verbose_name="Year")

    def __str__(self):
        return self.proj_name
    
    def get_hashed_id(self):
        return signing.dumps(self.proj_id)
    
    class Meta:
        db_table = "projects"


class Technology(models.Model):
    name = models.CharField(max_length=50)
    icon = ResizedImageField(
        force_format="WEBP",
        quality=80,
        upload_to='tech-icons/'
    )

    def __str__(self):
        return self.name
    

class Experience(models.Model):
    exp_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=100, verbose_name="Name")
    exp_desc = models.TextField(verbose_name="Description")
    date_serve = models.TextField(verbose_name="Employment Period")
    location = models.CharField(max_length=100, verbose_name="Location")
    tech_used = models.ManyToManyField(Technology, blank=True, related_name='experiences')

    def __str__(self):
        return self.position
    
    class Meta:
        db_table = "experiences"
