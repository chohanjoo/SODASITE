from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Post,Project
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'blog/index.html')


class ProjectListVew(ListView):
    model=Project
    template_name = "blog/post_list.html"
    context_object_name = 'post_list'   # your own name for the list as a template variable
    queryset = Project.objects.all().order_by('-id')

    paginate_by = 8
 
    def get_queryset(self, *args, **kwargs):
        if self.kwargs:
            return Project.objects.order_by('-id')
        else:
            post_list = Project.objects.all().order_by('-id')
            return post_list


   

post_list = ProjectListVew.as_view()


# def post_list(request):
#     post = Project.objects.all().order_by('-id')
#     return render(request,'blog/index.html', {
#         'post_list' : post
#     })

# class ProjectDetailView(DetailView):
#     model = Project
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'
#     queryset = Project.objects.get(pk=pk)

#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['tag_name'] = self.request.GET.get('get_parameter_name', None)
#         return ctx


def post_detail(request,pk):
    post = Project.objects.get(pk=pk)
    previous_post = Project.objects.filter(created_at=post.created_at).order_by('-created_at').first()
    # logger.info("pk %s".pk)
    return render(request, 'blog/post_detail.html',{
        'post' : post,
        'previous_post' : previous_post,
    })

# def new_post(request):
#     if request.method=='POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request, 'blog/new_post.html',{
#         'form' : form,
#     })

class NewPostView(LoginRequiredMixin,CreateView):
    model = Project
    form_class = PostForm
    template_name = 'blog/new_post.html'

new_post = NewPostView.as_view()


class EditPostView(UpdateView):
    model = Project
    form_class = PostForm
    template_name = 'blog/edit_post.html'


edit_post = EditPostView.as_view()


class DeletePostView(DeleteView):
    model = Project
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/delete_post.html'

   

delete_post = DeletePostView.as_view()