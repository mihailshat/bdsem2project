from django.db import models

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    duration_weeks = models.IntegerField()

    def __str__(self):
        return self.course_name

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    start_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    enrollment_year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Topic(models.Model):
    topic_name = models.CharField(max_length=255)
    topic_description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name

class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.resource_name


class Grade(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    grade = models.FloatField()
    date = models.DateField()
    note = models.TextField()

    def __str__(self):
        return f"{self.student} - {self.course}"


class CourseStudent(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('course', 'student')

    def __str__(self):
        return f"{self.student} - {self.course}"

class TopicResource(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('topic', 'resource')

    def __str__(self):
        return f"{self.topic} - {self.resource}"
    