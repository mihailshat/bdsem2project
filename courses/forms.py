from django import forms
from .models import Course
from .models import Student
from .models import Grade
from .models import Instructor
from .models import Topic
from .models import Resource


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'enrollment_year']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'instructor', 'start_date', 'duration_weeks']


class CourseFilterForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label=None)

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade', 'date', 'note']


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'email', 'contact_number', 'start_date']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_name', 'topic_description', 'course']


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['resource_name', 'resource_type', 'description', 'link']