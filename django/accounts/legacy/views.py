from django.shortcuts import render,resolve_url,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,UpdateView
from django.conf import settings
from django.contrib.auth.models import User
from .forms import SignupForm, ProfileForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm
)   


import logging
from .readExcel import readDataToExcel
from .models import Student,Profile

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token


from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags



logger = logging.getLogger(__name__)
# Create your views here.

def profile(request,pk):
    user_profile = Profile.objects.get(pk=pk)
    return render(request,'accounts/profile.html',{
        'profile': user_profile,
    })

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_edit.html'

profile_edit = ProfileEditView.as_view()


def user_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    try:
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect(settings.LOGIN_URL)
        else:
            return redirect(settings.LOGIN_URL)
    except Exception as e:
        print('error')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False

            try:
                student = Student.objects.get(name=user)
            except:
                student = None
            if student:
                user.save()
                # send email for new user
                subject = ('Welcome To Soda Site! Confirm Your Email')
                message = render_to_string('accounts/account_activate_email.html',{
                    'user' : student.name,
                    'domain' : 'localhost:8000',
                    'uid' : urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
                    'token' : account_activation_token.make_token(user)
                })

                text_content = strip_tags(message)
                
                send_to = [student.email]
                msg = EmailMultiAlternatives(subject, text_content, 'vjswl132@gmail.com', send_to)
                msg.attach_alternative(message,"text/html")
                msg.send()

            return redirect(settings.LOGIN_URL)
        else:
            ValidationError(_('Invalid value'), code='invalid')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{
        'form':form,
    })


class MyLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return resolve_url('blog:post_list')

    def form_valid(self,form):
        logger.debug('Login Success!!')
        auth_login(self.request, form.get_user())
        return redirect(self.get_success_url())

def index(request):
    return render(request,'blog/index.html')


@login_required
def inputDatabase(request):
    data = readDataToExcel()
    for person in data:
        Student(name=person['name'],studentNumber=person['studentNumber'],email=person['email']).save()

    return render(request,'accounts/init.html',{'data':data})