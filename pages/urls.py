from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('explore/', ExplorePageView.as_view(), name='explore'),
    path('explore/guide/<name>', CoursePageView.as_view(), name='course'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('explore/<name>/<id>', PostPageView.as_view(), name='post'),
]