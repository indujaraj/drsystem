from django.db import models
from django.utils import timezone

from centerhead.models import Course, Batch
from drsapp.models import MyUser


class Student(models.Model):
    ADMITTED = 'admitted'
    NOTINTERESTED = 'notinterested'
    FOLLOWUP = 'followup'
    STATUS = [
        (ADMITTED, 'Admitted'),
        (NOTINTERESTED, 'Notinterested'),
        (FOLLOWUP, 'Followup')

    ]
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='followup')
    followup_date = models.DateField(null=True,blank=True)
    enquiry_date = models.DateTimeField(default=timezone.now)
    telecaller = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering= ['-enquiry_date']

    def __str__(self):
        return self.name


