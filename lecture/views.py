from django.shortcuts import get_object_or_404,render,redirect, resolve_url
from django.http import HttpResponse
from .forms import LectureForm
from .models import Lecture, Professor
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
        print(form.__dict__["fields"]["professor"])

        # print(request.POST.get)
        if form.is_valid():
            print('1111')
            lecture = form.save()
            # p_name = form.cleaned_data.get('professor')
            # Professor.save()
            # lecture = form.save(commit=False)
            # lecture.professor = professor
            # lecture.save()

            return redirect(lecture)
        else :
            ValidationError(_('Invalid value'), code='invalid')

    else:
        form = form_cls()

    return render(request, template_name,{
        'form' : form,
    })

def detail_lecture(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    form = LectureForm(instance = lecture)
    template_name = 'lecture/lecture_detail.html'

    return render(request, template_name,{
        'form' : form,
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
