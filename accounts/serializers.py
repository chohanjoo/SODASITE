from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from rest_framework import serializers

from .tokens import account_activation_token

from simple_aes_cipher import AESCipher
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(max_length=64, required=False)
    updated_by =serializers.CharField(max_length=64, required=False)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password')
        def to_internal_value(self, data):
            ret = super(UserSerializer, self).to_internal_value(data)

            cipher = AESCipher()
            ret['password'] = cipher.encrypt_str(ret['password'])

            return ret

        def to_representation(self, obj):
            ret = super(UserSerializer, self).to_representation(obj)
            return ret

        def validate_email(self, value):
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("이메일이 이미 존재합니다.")
            return value
        
        def validate_password(self, value):
            if len(value) < 8:
                raise serializers.ValidationError("패스워드는 최소 %s자 이상이어야 합니다."%8)
            return value

        def create(self, validate_data):

            user = User.objects.create(
                username = validate_data['username'],
                password = validate_data['password']
            )

            user.is_active = False
            user.save()

            message = render_to_string('accounts/account_activate_email.html',{
                'user' : user,
                'domain' : 'localhost:8000',
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
                'token' : account_activation_token.make_token(user)
            })

            mail_subject = 'test'
            to_email = 'johanjoo@naver.com'
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return validate_data