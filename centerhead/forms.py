from django import forms

from centerhead.models import Course, Batch
from drsapp.models import MyUser


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = ['course_name', 'fee']


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch

        fields = ['course', 'batch','total_seats','remaining_seats']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = ['email', 'phone', 'role', ]



