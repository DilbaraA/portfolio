from django.urls import path
from rest_framework.routers import DefaultRouter as DR
from apps.cv.views import CvView, CategoryProjectView, ProjectImageView, ProjectView, ProjectStackView

urlpatterns = [

]


router= DR()
router.register('cv', CvView)
router.register('category', CategoryProjectView)
router.register('project', ProjectView)
router.register('projectimage', ProjectImageView)
router.register('projectstack', ProjectStackView)
urlpatterns += router.urls