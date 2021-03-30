from django.views.generic import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'

class ExplorePageView(TemplateView):
    template_name = 'explore.html'

class PostPageView(TemplateView):
    template_name = 'post.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class CoursePageView(TemplateView):
    template_name = 'course.html'
