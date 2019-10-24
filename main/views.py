from django.shortcuts import render
from blog.models import Project
from django.views.generic import ListView, DetailView
# Create your views here.

class ProjectListVew(ListView):
    model=Project
    template_name = 'main/index.html'
    context_object_name = 'post_list'   # your own name for the list as a template variable
    queryset = Project.objects.all().order_by('-id')

    paginate_by = 12
 
    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Project.objects.order_by('-id')
        else:
            post_list = Project.objects.all().order_by('-id')
            return post_list
            
    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectListVew, self).get_context_data(*args, **kwargs)
        # add whatever to your context:
        context['popular_post'] = Project.objects.all().order_by('-created_at')[:3]
        return context

index = ProjectListVew.as_view()