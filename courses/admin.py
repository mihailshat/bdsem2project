from django.contrib import admin
from .models import Course, Student, Grade, Instructor, Topic, Resource, CourseStudent, TopicResource

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'start_date', 'duration_weeks']
    list_filter = ['start_date']
    search_fields = ['course_name', 'course_description']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'enrollment_year']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'grade', 'date']
    list_filter = ['date']
    search_fields = ['student__first_name', 'student__last_name', 'course__course_name']

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'contact_number', 'start_date']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_name', 'course']
    search_fields = ['topic_name', 'course__course_name']

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['resource_name', 'resource_type', 'link']
    search_fields = ['resource_name', 'resource_type', 'description']

@admin.register(CourseStudent)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ['course', 'student']
    list_filter = ['course', 'student']
    search_fields = ['course__course_name', 'student__first_name', 'student__last_name']

@admin.register(TopicResource)
class TopicResourceAdmin(admin.ModelAdmin):
    list_display = ['topic', 'resource']
    list_filter = ['topic', 'resource']
    search_fields = ['topic__topic_name', 'resource__resource_name']