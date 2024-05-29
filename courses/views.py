from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student, Grade, Instructor, Topic, Resource, CourseStudent, TopicResource
from django.http import HttpResponse
from .forms import CourseForm, StudentForm, GradeForm, InstructorForm, TopicForm, ResourceForm

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('index')
    return render(request, 'delete_course.html', {'course': course})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

def course_students(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = Student.objects.filter(course=course)
    return render(request, 'course_students.html', {'course': course, 'students': students})


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'delete_student.html', {'student': student})


def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html', {'students': students})


def all_courses(request):
    courses = Course.objects.all()
    return render(request, 'all_courses.html', {'courses': courses})

def assign_student_to_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.course = course
            student.save()
            return redirect('course_detail', pk=course_id)
    else:
        form = StudentForm()
    return render(request, 'assign_student_to_course.html', {'form': form, 'course': course})



def edit_course_students(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = Student.objects.filter(course=course)
    if request.method == 'POST':
        formset = StudentFormSet(request.POST, queryset=students)
        if formset.is_valid():
            formset.save()
            return redirect('course_detail', pk=course_id)
    else:
        formset = StudentFormSet(queryset=students)
    return render(request, 'edit_course_students.html', {'formset': formset, 'course': course})


def students_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students_detail.html', {'student': student})


def all_grades(request):
    grades = Grade.objects.all()
    return render(request, 'all_grades.html', {'grades': grades})

def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_grades')
    else:
        form = GradeForm()
    return render(request, 'create_grade.html', {'form': form})



def all_instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'all_instructors.html', {'instructors': instructors})



def create_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_instructors')
    else:
        form = InstructorForm()
    return render(request, 'create_instructor.html', {'form': form})


def all_topics(request):
    topics = Topic.objects.all()
    return render(request, 'all_topics.html', {'topics': topics})

def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_topics')
    else:
        form = TopicForm()
    return render(request, 'create_topic.html', {'form': form})



def all_resources(request):
    resources = Resource.objects.all()
    return render(request, 'all_resources.html', {'resources': resources})

def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_resources')
    else:
        form = ResourceForm()
    return render(request, 'create_resource.html', {'form': form})




def students_for_course(request, course_id):
    course_students = CourseStudent.objects.filter(course_id=course_id)
    return render(request, 'students_for_course.html', {'course_students': course_students})

def courses_for_student(request, student_id):
    student_courses = CourseStudent.objects.filter(student_id=student_id)
    return render(request, 'courses_for_students.html', {'student_courses': student_courses})



def resources_for_topic(request, topic_id):
    topic_resources = TopicResource.objects.filter(topic_id=topic_id)
    return render(request, 'resources_for_topic.html', {'topic_resources': topic_resources})

def topics_for_resource(request, resource_id):
    resource_topics = TopicResource.objects.filter(resource_id=resource_id)
    return render(request, 'topics_for_resource.html', {'resource_topics': resource_topics})