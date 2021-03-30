from django.db import models

# Create your models here.
class DivisionGuide(models.Model):
    divisionName = models.CharField(max_length=20, unique= True)
    guideLinks = models.URLField()

class Project(models.Model):
    divisionName = models.ForeignKey(DivisionGuide, on_delete=models.CASCADE)
    projectName = models.CharField(unique= True, max_length=200)
    projectThumbnailpic = models.CharField(unique= True, max_length=200)  #has pic name
    projectStepsLink = models.URLField(max_length= 255)
    projectImagesLink = models.URLField(max_length= 255)
    projectCodesLink = models.URLField(max_length=255)
    projectStepsLink = models.URLField(max_length=255)