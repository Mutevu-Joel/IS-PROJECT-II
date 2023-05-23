from pyexpat import model
from tkinter import TRUE

import django_filters
from django.forms import DateInput

from .models import Child
from .forms import *
from itertools import chain


class ChildFilter(django_filters.FilterSet):
    return_date = django_filters.DateFilter(
        widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )
    immunized_at = django_filters.DateFilter(
        widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )

    class Meta:
        model = Child
        fields = '__all__'
        include = ['dob', 'surname', 'other_name', 'village']
        exclude = ['weight', 'height', 'parent_id', 'comment']


class ParentFilter(django_filters.FilterSet):
    class Meta:
        model = Parent
        fields = '__all__'
        exclude = ['parent_id', 'mobile_no', 'dob', 'surname', 'other_name', 'village']
