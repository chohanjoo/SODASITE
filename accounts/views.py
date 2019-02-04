from django.shortcuts import render,resolve_url,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.conf import settings
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import login as auth_login
# Create your views here.

@login_required
def profile(request):
    return render(request,'accounts/profile.html')


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self,form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()
# signup = CreateView.as_view(model=User, form_class=UserCreationForm
#         , success_url = settings.LOGIN_URL
#         ,template_name="accounts/signup.html")