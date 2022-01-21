from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=120, unique=True)
    active_status = models.BooleanField(default=True)
    fee = models.PositiveIntegerField()

    def __str__(self):
        return self.course_name


class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    batch = models.CharField(max_length=120)
    active_status = models.BooleanField(default=True)
    total_seats = models.PositiveIntegerField(null=True)
    remaining_seats = models.PositiveIntegerField(null=True)



    def __str__(self):
        return self.batch
