from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = get_user_model()
# Create your models here.
class Cv(models.Model):
    name = models.CharField(max_length=127)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='cvs')
    cv = models.FileField(upload_to= 'cv/file')
    email = models.CharField(max_length=127)
    phone_number = models.CharField(max_length=13)
    work_experience = models.TextField()
    stack = models.CharField(max_length=127)
    level = models.CharField(max_length=127)
    vacancy = models.CharField(max_length=127)
    avatar = models.ImageField()


class CategoryProject(models.Model):
    name = models.CharField(max_length=127)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='categoryprojects')
    description = models.TextField()
    image = models.ImageField()


class Project(models.Model):
    name = models.CharField(max_length=127)
    category = models.ForeignKey(to=CategoryProject, on_delete=models.CASCADE, related_name='projects' )
    description = models.TextField()
    image = models.ImageField()
    link = models.URLField()
    link_code = models.URLField(null=True, blank=True)
    time_development = models.TimeField()


class ProjectImage(models.Model):
    project = models.ForeignKey(to = Project, on_delete=models.CASCADE, related_name='projectimages')
    image = models.ImageField()


class ProjectStack(models.Model):
    project = models.ForeignKey(to = Project, on_delete=models.CASCADE, related_name='projectstacks')
    name = models.CharField(max_length=127)
    
    





