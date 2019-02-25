from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Post,Project
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import PostForm
# Create your views here.
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'blog/index.html')

# post_list = ListView.as_view(model=Post)

def post_list(request):
    post = Project.objects.all().order_by('-id')
    return render(request,'blog/index.html', {
        'post_list' : post
    })

def post_detail(request,pk):
    post = Project.objects.get(pk=pk)
    # logger.info("pk %s".pk)
    return render(request, 'blog/post_detail.html',{
        'post' : post
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

class NewPostView(CreateView):
    model = Project
    form_class = PostForm
    template_name = 'blog/new_post.html'

new_post = NewPostView.as_view()
# new_post = CreateView.as_view(model=Project, form_class=PostForm, template_name = 'blog/new_post.html', success_url = "{% url "blog:post_list" %}")
# def edit_post(request):
#     return render(request, 'blog/edit_post.html')
# post_detail = DetailView.as_view(model=Post)

# @login_required
# def post_new(request):
#     pass

class EditPostView(UpdateView):
    model = Project
    form_class = PostForm
    template_name = 'blog/edit_post.html'


edit_post = EditPostView.as_view()


class DeletePostView(DeleteView):
    model = Project
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/delete_post.html'

    # def get_queryset(self):
    #     queryset = super(ChargeParkConfirmDeleteView, self).get_queryset()
    #     self.queryset = queryset.filter(id__in=self.items_to_delete)
    #     return self.queryset

    # def get_object(self, queryset=None):
    #     return self.get_queryset()

    # def post(self, request, *args, **kwargs):
    #     self.items_to_delete = self.request.POST.getlist('itemsToDelete')
    #     if self.request.POST.get("confirm_delete"):
    #         # when confirmation page has been displayed and confirm button pressed
    #         queryset = self.get_queryset()
    #         queryset.delete() # deleting on the queryset is more efficient than on the model object
    #         return HttpResponseRedirect(self.success_url)
    #     elif self.request.POST.get("cancel"):
    #         # when confirmation page has been displayed and cancel button pressed
    #         return HttpResponseRedirect(self.success_url)
    #     else:
    #         # when data is coming from the form which lists all items
    #         return self.get(self, *args, **kwargs)

delete_post = DeletePostView.as_view()