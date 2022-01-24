from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from centerhead.models import Batch
from telecaller.forms import LoginForm, StudentForm
from drsapp.admin import UserCreationForm
from drsapp.models import MyUser
from telecaller.models import Student





class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'studentform.html'
    success_url = reverse_lazy('studentcreate')

    def form_valid(self, form):
        form.instance.telecaller = self.request.user
        if form.instance.status == 'admitted':
            batch = Batch.objects.get(id=form.data.__getitem__('batch'))
            if batch.remaining_seats == 0:
                error = True
                messages.error(self.request, 'SORRY!! No seat available for the selected course')
                return redirect('studentcreate')
            else:
                batch.remaining_seats = batch.remaining_seats - 1
                batch.save()
        return super(StudentCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.model.objects.all()

        return context


def load_cities(request):
    course_id = request.GET.get('course_id')
    print(course_id)
    cities = Batch.objects.filter(course_id=course_id).all()
    print(cities)
    return render(request, 'coursebatch.html', {'cities': cities})


class EnquiriesList(ListView):
    model = Student
    form_class = StudentForm
    template_name = 'enquirieslist.html'
    context_object_name = 'enquiries'


class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'updatestudent.html'
    success_url = reverse_lazy('studentcreate')
    pk_url_kwarg = 'id'

    def form_valid(self, form):

        if form.instance.status == 'admitted':
            batch = Batch.objects.get(id=form.data.__getitem__('batch'))
            if batch.remaining_seats == 0:
                error = True
                messages.error(self.request, 'SORRY!! No seat available for the selected course')
                return redirect('enquirieslist')
            else:
                batch.remaining_seats = batch.remaining_seats - 1
                batch.save()
        return super(StudentUpdate, self).form_valid(form)


class StudentDelete(DeleteView):
    model = Student
    template_name = 'deletestudent.html'
    success_url = reverse_lazy('studentcreate')
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = context['student']
        if student.status == 'admitted':
            batch = Batch.objects.get(id=student.batch.id)
            batch.remaining_seats += 1
            batch.save()

            return context


class TeleHome(TemplateView):
    template_name = 'telehome.html'


class BatchList(ListView):
    model = Batch
    context_object_name = 'batches'
    template_name = 'batchlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['batches'] = self.model.objects.all()

        return context
