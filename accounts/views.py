from django.shortcuts import render,resolve_url,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.conf import settings
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import (
    AuthenticationForm
)   
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

import logging
from .readExcel import readDataToExcel
from .models import Student

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from .serializers import UserSerializer

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token


logger = logging.getLogger(__name__)
# Create your views here.

@login_required
def profile(request):
    return render(request,'accounts/profile.html')

# class SignUp(APIView):
    
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# signup = SignUp.as_view()

# class UserActivate(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def get(self, requset, uidb64, token):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64.encode('utf-8')))
#             user = User.objects.get(pk=uid)
#         except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
        
#         try:
#             if user is not None and account_activation_token.check_token(user, token):
#                 user.is_active = True
#                 user.save()
#                 return Response(user.email + '계정이 활성화 되었습니다.', status=status.HTTP_200_OK)
#             else:
#                 return Response('만료된 링크입니다.', status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             print('error')

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
            return redirect('/blog/')
        else:
            return redirect('/blog/')
    except Exception as e:
        print('error')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            try:
                student = Student.objects.get(name=user)
            except:
                student = None
            if student:

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
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{
        'form':form,
    })
# class SignupView(CreateView):
#     model = User
#     form_class = SignupForm
#     template_name = 'accounts/signup.html'

#     def get_success_url(self):
#         return resolve_url('blog:index')

#     def form_valid(self,form):
#         logger.debug('Here is Create ID')
#         user = form.save()
#         auth_login(self.request, user)
#         return redirect(self.get_success_url())

#signup = SignupView.as_view()
# signup = CreateView.as_view(model=User, form_class=UserCreationForm
#         , success_url = settings.LOGIN_URL
#         ,template_name="accounts/signup.html")

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


def inputDatabase(request):
    data = readDataToExcel()
    for person in data:
        Student(name=person['name'],studentNumber=person['studentNumber'],email=person['email']).save()

    return render(request,'accounts/init.html',{'data':data})