from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
import datetime

class Lecture(models.Model):
    name = models.CharField(verbose_name = '강의명', max_length = 50)
    professor = models.CharField(verbose_name = '교수님', max_length = 50)
    year = models.IntegerField(verbose_name = '수강년도')
    semester = models.IntegerField(verbose_name = '수강학기')
    evalue = models.TextField(verbose_name = '강의평')
    examfile = models.FileField(blank = True, upload_to= 'lecture', verbose_name = '족보파일')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lecture:detail_lecture', args=[self.pk])
    

    # def save(self, **kwargs):
    #     professor = Professor.objects.get_or_create(name = self.professor)
    #     print(professor)
    #     super(Lecture, self).save(**kwargs)



