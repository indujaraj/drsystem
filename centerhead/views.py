from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DeleteView

from centerhead.forms import CourseForm, BatchForm
from centerhead.models import Course, Batch
from drsapp.admin import UserCreationForm
from drsapp.models import MyUser
from telecaller.models import Student


class AdminHome(TemplateView):
    template_name = 'adminhome.html'


class CourseCreate(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courseform.html'
    success_url = reverse_lazy('coursecreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.model.objects.all()
        return context


class BatchCreate(CreateView):
    model = Batch
    form_class = BatchForm
    template_name = 'batchform.html'
    success_url = reverse_lazy('batchcreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batches'] = self.model.objects.all()

        for batch in context['batches']:
            students = Student.objects.filter(batch=batch)
            for student in students:
                if student.status == 'admitted':
                    batch.remaining_seats -= 1

        return context


class TelecallerList(ListView):
    model = MyUser
    template_name = 'telecallerlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['telecallers'] = self.model.objects.exclude(is_admin=True)
        return context


def loghome(request):
    if request.user.is_authenticated:
        if request.user.role == 'admin':
            return redirect('centerhead/adminhome')
        else:
            return redirect('telecaller/telehome')
    return render(request, 'registration/loghome.html')


class TeleCallerDelete(DeleteView):
    model = MyUser
    template_name = 'deletetelecaller.html'
    success_url = reverse_lazy('telecallerlist')
    pk_url_kwarg = 'id'
