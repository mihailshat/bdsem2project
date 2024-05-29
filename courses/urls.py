from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/create/', views.create_course, name='create_course'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/<int:pk>/edit/', views.edit_course, name='edit_course'),
    path('course/<int:pk>/delete/', views.delete_course, name='delete_course'),
    path('course/<int:pk>/students/', views.course_students, name='course_students'),
    path('student/create/', views.create_student, name='create_student'),
    path('student/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('students/', views.all_students, name='all_students'),
    path('courses/', views.all_courses, name='all_courses'),
    path('course/<int:course_id>/assign_student/', views.assign_student_to_course, name='assign_student_to_course'),
    path('course/<int:course_id>/edit_students/', views.edit_course_students, name='edit_course_students'),
    path('student/<int:pk>/', views.students_detail, name='students_detail'),
    path('grades/', views.all_grades, name='all_grades'),
    path('grades/create/', views.create_grade, name='create_grade'),
    path('instructors/', views.all_instructors, name='all_instructors'),
    path('instructors/create/', views.create_instructor, name='create_instructor'),

    path('topics/', views.all_topics, name='all_topics'),
    path('topics/create/', views.create_topic, name='create_topic'),

    path('resources/', views.all_resources, name='all_resources'),
    path('create_resource/', views.create_resource, name='create_resource'),

    path('resources_for_topic/<int:topic_id>/', views.resources_for_topic, name='resources_for_topic'),
    path('topics_for_resource/<int:resource_id>/', views.topics_for_resource, name='topics_for_resource'),

    path('students/<int:course_id>/', views.students_for_course, name='students_for_course'),
    path('courses/<int:student_id>/', views.courses_for_student, name='courses_for_students'),

]

