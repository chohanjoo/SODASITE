from django.shortcuts import get_object_or_404,render,redirect, resolve_url
from django.http import HttpResponse
from .forms import LectureForm
from .models import Lecture
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os
from django.conf import settings

def index(request):
    lecture_list = Lecture.objects.all().order_by('name')
    template_name = 'lecture/lecture_list.html'
    
    return render(request, template_name, {
        'lecture_list' : lecture_list,
    })

def add_lecture(request):
    form_cls = LectureForm
    template_name = 'lecture/lecture_add.html'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES)
        files = request.FILES.getlist('examfile')
        if form.is_valid():
            for f in files:
                tmp = open(os.path.join(os.getcwd(), 'media/lecture', f.name), 'wb+')
                for chunk in f.chunks():
                    tmp.write(chunk)
            lecture = form.save()
            return redirect(lecture)
        else :
            ValidationError(_('Invalid value'), code='invalid')

    else:
        form = form_cls()

    return render(request, template_name,{
        'form' : form,
    })

def detail_lecture(request, pk):
    lecture = Lecture.objects.get(pk=pk)
    form = LectureForm(instance = lecture)
    template_name = 'lecture/lecture_detail.html'
    return render(request, template_name,{
        'form' : form
    })

def edit_lecture(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    form_cls = LectureForm
    template_name = 'lecture/lecture_edit.html'

    if request.method == 'POST':
        form = form_cls(request.POST, request.FILES, instance = lecture)

        if form.is_valid():
            lecture = form.save()
            return redirect(lecture)

    else:
        form = form_cls(instance = lecture)

    return render(request, template_name,{
        'form' : form,
    })

def delete_lecture(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    lecture.delete()

    return redirect('/lecture')