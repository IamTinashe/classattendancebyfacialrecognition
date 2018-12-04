from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mysite.core.models import Students


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AddDepartment(forms.Form):
    department = forms.CharField(label='Department', max_length=120)


class AddStudents(forms.ModelForm):
	class Meta:
        	model = Students
        	fields = ('student_number', 'student_name', 'student_surname', 'student_year', 'student_picture', 'department_id',)
