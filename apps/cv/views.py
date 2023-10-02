
from rest_framework.views import APIView

from apps.cv.models import Cv, CategoryProject, Project, ProjectStack,ProjectImage
from apps.cv.serializers import CvSerializers,CategoryProjectSerializer,ProjectSerializer,ProjectStackSerializer,ProjectImageSerializer
from rest_framework.viewsets import ModelViewSet

class CvView(ModelViewSet):
    queryset = Cv.objects.all()
    serializer_class= CvSerializers

class CategoryProjectView(ModelViewSet):
    queryset = CategoryProject.objects.all()
    serializer_class = CategoryProjectSerializer

class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectStackView(ModelViewSet):
    queryset = ProjectStack.objects.all()
    serializer_class = ProjectStackSerializer

class ProjectImageView(ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer