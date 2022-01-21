from django import forms

from centerhead.models import Course, Batch
from telecaller.models import Student


class StudentForm(forms.ModelForm):
    followup_date = forms.DateInput(attrs={"type": "date"})

    class Meta:
        model = Student

        fields = ['name', 'email', 'contact', 'course', 'batch', 'status', 'followup_date', 'enquiry_date']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['batch'].queryset = Course.objects.none()

        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['batch'].queryset = Batch.objects.filter(course_id=course_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['batch'].queryset = self.instance.course.batch_set.order_by('batch_name')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
