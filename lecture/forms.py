from django import forms
from .models import Lecture
import datetime

class LectureForm(forms.ModelForm):
    SEMESTER = (
        (0,'1학기'),
        (1,'여름방학'),
        (2,'2학기'),
        (3,'겨울방학'),
    )
    YEAR_CHOICES = [(y,y) for y in range(2012, datetime.date.today().year+1)]

    year = forms.IntegerField(widget = forms.Select(choices=YEAR_CHOICES), label = '수강년도')
    semester = forms.IntegerField(widget = forms.Select(choices=SEMESTER), label = '수강학기')

    def __init__(self, *args, **kwargs):
        super(LectureForm, self).__init__(*args, **kwargs)
        self.initial['year'] = datetime.date.today().year

    class Meta:
        model = Lecture
        fields = ['name','professor','year','semester','evalue','examfile']
