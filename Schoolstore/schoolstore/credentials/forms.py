from django import forms
from .models import Enrollment, Department


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'


class ProductForm(forms.Form):
    Departments = forms.ModelChoiceField(queryset=Department.objects.all())
    Course = forms.ChoiceField(choices=[])
