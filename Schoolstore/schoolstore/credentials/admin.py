from django.contrib import admin

from django.contrib import admin

# Register your models here.
from . models import Department,Course,Enrollment,Material

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Course,CourseAdmin)
admin.site.register(Enrollment)
admin.site.register(Material)
