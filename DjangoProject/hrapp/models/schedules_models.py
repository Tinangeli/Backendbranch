from django.db import models
from .user_models import User

# Courses
class Course(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete support
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.name} - {self.code} - {self.slug} - {self.is_active} - {self.created_at} - {self.updated_at} - {self.deleted_at}'

    def restore(self):
        self.deleted_at = None
        self.save()

# Subjects
class Subject(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete support
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.name} - {self.slug} - {self.is_active} - {self.created_at} - {self.updated_at} - {self.deleted_at}'

    def restore(self):
        self.deleted_at = None
        self.save()


# Rooms
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete support
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.name} - {self.slug} - {self.is_active} - {self.created_at} - {self.updated_at} - {self.deleted_at}'

    def restore(self):
        self.deleted_at = None
        self.save()

# Schedules
class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)  # Deletes schedule if course is removed
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Links professor to schedule
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    SEMESTER_CHOICES = [('First', 'First'), ('Second', 'Second'), ('Summer', 'Summer')]
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    year = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)  # Soft delete support
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'{self.course} - {self.professor} - {self.subject} - {self.room} - {self.name} - {self.start_time} - {self.end_time} - {self.semester} - {self.year} - {self.year} - {self.is_active} - {self.deleted_at}'

    def restore(self):
        self.deleted_at = None
        self.save()


# Faculty Assignments
class FacultyAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Assigns faculty to schedule
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f'{self.user} - {self.schedule} - {self.created_at} - {self.updated_at} - {self.deleted_at}'

    def restore(self):
        self.deleted_at = None
        self.save()

