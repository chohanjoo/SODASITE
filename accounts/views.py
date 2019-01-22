from django.shortcuts import render,redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import login as auth_login
# Create your views here.


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

# def signup(request):
    # if request.method == "POST":
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()

    #            #로그인 처리
    #            auth_login(request, user) 
    #         return redirect(settings.LOGIN_URL)
    # else:
    #     form = SignupForm()

    # return render(request, 'accounts/signup.html',{
    #     'form' : form,
    # })

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
