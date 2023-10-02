from rest_framework import serializers
from apps.cv.models import Cv, CategoryProject, Project, ProjectImage, ProjectStack
from apps.cv.models import User
from apps.users.serializer import UserSerializers


class CvSerializers(serializers.ModelSerializer):
    cvs = UserSerializers(many=True, read_only = True)
    class Meta:
        model = Cv
        fields = (
            'name',
            'user',
            'cv',
            'email',
            'phone_number',
            'work_experience',
            'stack',
            'level',
            'vacancy',
            'avatar',
            'cvs'
        )

class CategoryProjectSerializer(serializers.ModelSerializer):
    categoryprojects = UserSerializers(many = True,read_only = True)
    class Meta:
        model = CategoryProject
        fields = (
            'name',
            'user',
            'description',
            'image',
            'categoryprojects'
        )


class ProjectSerializer(serializers.ModelSerializer):
    projects = CategoryProjectSerializer(many = True, read_only = True)
    class Meta:
        model = Project
        fields = (
            'name',
            'category',
            'description',
            'image',
            'link',
            'link_code',
            'time_development',
            'projects'
        )


class ProjectImageSerializer(serializers.ModelSerializer):
    projectimages = ProjectSerializer(many = True, read_only = True)
    class Meta:
        model = ProjectImage
        fields = (
            'project',
            'image',
            'projectimages'
        )


class ProjectStackSerializer(serializers.ModelSerializer):
    projectstacks = ProjectSerializer(many = True, read_only = True)
    class Meta:
        model = ProjectStack
        fields = (
            'project',
            'name',
            'projectstacks'
        )


    





