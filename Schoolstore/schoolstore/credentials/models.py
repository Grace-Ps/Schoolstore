from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    wikipedia_link = models.URLField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('credentials:Course_by_department', args=[self.slug])

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return '{}'.format(self.name)




class Enrollment(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=50)
    courses = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    materials_provide = models.ManyToManyField('Material', blank=True)

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





# Create your models here.
